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
    'fd'
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
  #sudo mkdir -p /usr/local/spectrumos
  #sudo chown -R $USER:$USER /usr/local/spectrumos
  #sudo chmod 775 /usr/local/spectrumos
  cp -v -r ~/dotfiles/.config/qtile/* ~/.config/qtile/
  # cp -r ~/dotfiles/.config/gromit-mpx.cfg ~/.config/
  # cp -r ~/dotfiles/.config/xsettingsd/xsettingsd.conf ~/.config/xsettingsd/
  # mkdir -p ~/.icons
  # cp -r ~/dotfiles/.icons/* ~/.icons/
  # cp -r ~/dotfiles/.local/bin/* ~/.local/bin
  #cp -r ~/dotfiles/.local/bin/selectwal ~/.local/bin
  #cp -r ~/dotfiles/.local/bin/weather ~/.local/bin
  #cp -r ~/dotfiles/.local/bin/alwaystart ~/.local/bin
  #cp -r ~/dotfiles/.local/bin/wifi2 ~/.local/bin
  # chmod +x ~/.local/bin/*
  # cp ~/dotfiles/.zshrc ~/
  # mkdir -p  ~/.config/flameshot
  # cp ~/dotfiles/.config/flameshot/flameshot.ini ~/.config/wal/templates
  # cp ~/dotfiles/.config/conky/* ~/.config/wal/templates
  # cp ~/dotfiles/.config/alacritty/alacritty.toml ~/.config/alacritty/alacritty.toml
  cp -v -r ~/dotfiles/.config/rofi/* ~/.config/rofi/
  # cp ~/dotfiles/.config/rofi/SpectrumOS.rasi ~/.config/wal/templates
  # cp ~/dotfiles/.config/cava/config ~/.config/wal/templates
  #cp ~/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
  # cp ~/dotfiles/.shortcuts ~/
  # sudo cp ~/dotfiles/logid.cfg /etc/
  cp ~/dotfiles/.config/dunst/dunstrc ~/.config/wal/templates
  # cp ~/dotfiles/.config/neofetch/config.conf ~/.config/neofetch/

  ### Add new Lightdm Theme

  #sudo cp -v ~/dotfiles/lightdm/lightdm.conf /etc/lightdm/
  #sudo cp -v ~/dotfiles/lightdm/lightdm-webkit2-greeter.conf  /etc/lightdm
  #sudo cp -v -r ~/dotfiles/lightdm/theme/SpectrumOS /usr/share/lightdm-webkit/themes/
}

#install_new_packages
#aur_packages
update

