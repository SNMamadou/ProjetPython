#!/bin/bash

# Variables
VM_NAME="ubuntu-server-vm"
ISO_PATH="./ubuntu-24.04.2-live-server-amd64.iso"
DISK_PATH="$HOME/${VM_NAME}.vdi"
DISK_SIZE="10240"  # 10 GB in MB
RAM="2048"
CPU="2"
PRESEED_FILE="./preseed.cfg"
PRESEED_IMG="./preseed.img"
PI_SCRIPT="./pi.sh"

# Check if the ISO exists
if [[ ! -f "$ISO_PATH" ]]; then
    echo "Error: The ISO $ISO_PATH does not exist."
    exit 1
fi

# Create the disk if it doesn't exist
if [[ ! -f "$DISK_PATH" ]]; then
    echo "Creating disk $DISK_PATH..."
    VBoxManage createhd --filename "$DISK_PATH" --size $DISK_SIZE --format VDI
else
    echo "Disk $DISK_PATH already exists."
fi

# Check if the VM already exists
if VBoxManage list vms | grep -q "\"$VM_NAME\""; then
    echo "VM $VM_NAME already exists."
else
    # Create the VM if it doesn't exist
    echo "Creating VM $VM_NAME..."
    VBoxManage createvm --name "$VM_NAME" --register
    VBoxManage modifyvm "$VM_NAME" --memory "$RAM" --cpus "$CPU" --ostype Ubuntu_64 --nic1 nat
fi

# Check if the SATA controller already exists
if VBoxManage showvminfo "$VM_NAME" | grep -q "SATA Controller"; then
    echo "SATA Controller already exists."
else
    # Add a SATA controller only if it doesn't already exist
    echo "Adding SATA Controller to VM $VM_NAME..."
    VBoxManage storagectl "$VM_NAME" --name "SATA Controller" --add sata --controller IntelAHCI
fi

# Create the floppy image for the preseed file and pi.sh script
echo "Creating floppy image for the preseed file and pi.sh script..."
dd if=/dev/zero of="$PRESEED_IMG" bs=1M count=1
mkfs.vfat "$PRESEED_IMG"
mkdir -p /mnt/floppy
sudo mount -o loop "$PRESEED_IMG" /mnt/floppy
sudo cp "$PRESEED_FILE" /mnt/floppy/
sudo cp "$PI_SCRIPT" /mnt/floppy/
sudo umount /mnt/floppy
rmdir /mnt/floppy

# Attach the disk, ISO, and preseed file
echo "Attaching disk, ISO, and preseed file..."
VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$DISK_PATH"
VBoxManage storageattach "$VM_NAME" --storagectl "SATA Controller" --port 1 --device 0 --type dvddrive --medium "$ISO_PATH"
VBoxManage storageattach "$VM_NAME" --storagectl "IDE Controller" --port 0 --device 1 --type floppy --medium "$PRESEED_IMG"

# Configure boot settings to use the preseed file and auto install
echo "Configuring boot settings to use the preseed file and auto install..."
VBoxManage setextradata "$VM_NAME" "VBoxInternal2/EFIBootArgs" "auto preseed/file=/hd-media/preseed.cfg interface=auto"

# Start the VM in headless mode (without GUI)
echo "Starting VM $VM_NAME..."
VBoxManage startvm "$VM_NAME" --type headless
