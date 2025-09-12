Vagrant.configure("2") do |config|
  nodes = {
    "vm1" => "192.168.56.101",
    "vm2" => "192.168.56.102"
  }

  nodes.each do |name, ip|
    config.vm.define name do |node|
      node.vm.box = "debian/bookworm64"
      node.vm.hostname = name
      node.vm.network "private_network", ip: ip

      node.vm.provision "shell", inline: <<-SHELL
        echo "➡️ Installation des paquets requis (curl, bc, bash)..."
        apt-get update -qq
        apt-get install -y curl bc bash

        echo "⬇️ Téléchargement de pi.sh..."
        curl -s -O https://www-lipn.univ-paris13.fr/~cerin/pi.sh
        chmod +x pi.sh

        echo "▶️ Exécution de pi.sh avec bash..."
        bash ./pi.sh > result.txt
      SHELL
    end
  end
end
