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
  cp -r ~/SpectrumOS/dotfiles/.config/rofi/* ~/.config/rofi/
  
  cp -r ~/SpectrumOS/dotfiles/.config/qtile/* ~/.config/qtile/
  cp ~/SpectrumOS/dotfiles/.shortcuts ~/
  # cp -r ~/SpectrumOS/dotfiles/.local/bin/recorder ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/notesfi ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/wifi2 ~/.local/bin/
  #cp -r ~/SpectrumOS/dotfiles/.local/bin/recorder ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/selectwal ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/calculator ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/calendar ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/change_display ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/todo ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/autostart ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/alwaystart ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/bluet ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/genwal ~/.local/bin/
  cp -r ~/SpectrumOS/dotfiles/.local/bin/cleansys ~/.local/bin/
  chmod +x ~/.local/bin/*
  # cp ~/SpectrumOS/dotfiles/.shortcuts ~/

  cp ~/SpectrumOS/dotfiles/.config/rofi/SpectrumOS.rasi ~/.config/wal/templates
  #cp ~/SpectrumOS/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
  cp ~/SpectrumOS/dotfiles/.zshrc ~/
  cp ~/SpectrumOS/dotfiles/.config/dunst/dunstrc ~/.config/wal/templates
  cp ~/SpectrumOS/dotfiles/.config/flameshot/flameshot.ini ~/.config/wal/templates
  # cp ~/SpectrumOS/dotfiles/.config/cava/config ~/.config/wal/templates
  # cp ~/SpectrumOS/dotfiles/.config/ranger/rc.conf ~/.config/ranger/rc.conf
  # cp ~/SpectrumOS/dotfiles/.config/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml
  # cp ~/SpectrumOS/dotfiles/.config/gromit-mpx.ini ~/.config
  cp ~/SpectrumOS/dotfiles/.oh-my-zsh/themes/avit.zsh-theme ~/.oh-my-zsh/themes
}

#install_new_packages
#aur_packages
update