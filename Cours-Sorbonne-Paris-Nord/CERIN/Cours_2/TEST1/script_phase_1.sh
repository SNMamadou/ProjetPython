#!/bin/bash

# Variables
VM_NAME="debian-vm"
ISO_PATH="./debian-12.10.0-amd64-netinst.iso"
DISK_PATH="$HOME/${VM_NAME}.vdi"
DISK_SIZE="10240"  # 10 Go en Mo
RAM="2048"
CPU="2"
PRESEED_PATH="./preseed.cfg"

# Vérifier si l'ISO existe
if [[ ! -f "$ISO_PATH" ]]; then
    echo "Erreur : L'ISO $ISO_PATH n'existe pas."
    exit 1
fi

# Créer le disque si inexistant
if [[ ! -f "$DISK_PATH" ]]; then
    echo "Création du disque $DISK_PATH..."
    VBoxManage createhd --filename "$DISK_PATH" --size $DISK_SIZE --format VDI
else
    echo "Le disque $DISK_PATH existe déjà."
fi

# Vérifier si la VM existe déjà
if VBoxManage list vms | grep -q "\"$VM_NAME\""; then
    echo "La VM $VM_NAME existe déjà."
else
    # Créer la VM si elle n'existe pas
    echo "Création de la VM $VM_NAME..."
    VBoxManage createvm --name "$VM_NAME" --register
    VBoxManage modifyvm "$VM_NAME" --memory "$RAM" --cpus "$CPU" --ostype Debian_64 --nic1 nat
fi

# Vérifier si le contrôleur SATA existe déjà
if VBoxManage showvminfo "$VM_NAME" | grep -q "SATA Controller"; then
    echo "Le contrôleur SATA existe déjà."
else
    # Ajouter un contrôleur SATA uniquement s'il n'existe pas déjà
    echo "Ajout du contrôleur SATA à la VM $VM_NAME..."
    VBoxManage storagectl "$VM_NAME" --name "SATA Controller" --add sata --controller IntelAHCI
fi

# Attacher le disque, l'ISO et le fichier preseed
echo "Attachement du disque, de l'ISO et du fichier preseed..."
VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$DISK_PATH"
VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium "$ISO_PATH"
VBoxManage storageattach "$VM_NAME" --storagectl "IDE Controller" --port 0 --device 1 --type floppy --medium "$PRESEED_PATH"

# Démarrer la VM en mode headless (sans interface graphique)
echo "Démarrage de la VM $VM_NAME..."
VBoxManage startvm "$VM_NAME" --type headless
