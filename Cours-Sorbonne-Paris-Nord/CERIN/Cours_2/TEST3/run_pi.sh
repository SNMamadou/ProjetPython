#!/bin/bash

echo "▶️ Démarrage des VMs avec Vagrant..."
vagrant up

echo
echo "✅ VMs démarrées. Récupération des résultats..."
echo

# Récupération des résultats depuis vm1 et vm2
PI_VM1=$(vagrant ssh vm1 -c "cat result.txt" 2>/dev/null | grep -oP '[0-9]+\.[0-9]+')
PI_VM2=$(vagrant ssh vm2 -c "cat result.txt" 2>/dev/null | grep -oP '[0-9]+\.[0-9]+')

echo "🔎 Résultat depuis vm1 : $PI_VM1"
echo "🔎 Résultat depuis vm2 : $PI_VM2"

# Vérifie si les deux valeurs existent avant le calcul
if [[ -n "$PI_VM1" && -n "$PI_VM2" ]]; then
  # Calcul de la somme avec `bc`
  SUM=$(echo "$PI_VM1 + $PI_VM2" | bc -l)
  echo
  echo "🧮 Somme des deux valeurs de π : $SUM"
else
  echo
  echo "❌ Impossible de récupérer les deux valeurs. Vérifie les fichiers result.txt."
fi

echo -e "\n🧹 Destruction des VMs..."
vagrant destroy -f
