#!/usr/bin/env bash
# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#

function install_new_packages() {
  packets=(
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}

function aur_packages() {
  packets=(
    'rofi-file-browser-extended-git'
)
for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function update(){
  sudo mkdir -p /usr/local/spectrumos
  sudo chown -R $USER:$USER /usr/local/spectrumos
  sudo chmod 775 /usr/local/spectrumos
  cp ~/SpectrumOS/dotfiles/.config/qtile/variables /usr/local/spectrumos
  cp ~/SpectrumOS/dotfiles/.config/qtile/update /usr/local/spectrumos
  cp -r ~/SpectrumOS/dotfiles/.config/qtile/* ~/.config/qtile/
  cp -r ~/SpectrumOS/dotfiles/.config/xsettingsd/xsettingsd.conf ~/.config/xsettingsd/
  mkdir -p ~/.icons
  cp -r ~/SpectrumOS/dotfiles/.icons/* ~/.icons/
  cp ~/SpectrumOS/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
}

#install_new_packages
#aur_packages
update