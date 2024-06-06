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
#

# First Steps

## Install Dependencies

function base_install(){
    packets=(
        xorg-minimal
        xorg-fonts
        xinit
        elogind
        dbus-elogind
        polkit
        qtile
        python3-qtile-extras
        alacritty
        vim
        xf86-video-vmware # Use Correct for Video Card
        git
        curl
        zsh
        thefuck
        pywal
        setxkbmap
        bc
        picom
        iproute2
        inetutils

    )
for packet in "${packets[@]}"; do
    sudo xbps-install -Sy "${packet}"
done

}

## Install Qtile

function qtile_install(){
echo "exec /usr/bin/qtile start" > ~/.xinitrc
mkdir -p ~/Pictures/Wallpapers
cp ~/dotfiles/Wallpapers/wall.png ~/Pictures/Wallpapers
mkdir -p ~/.config/picom
cp ~/dotfiles/.config/picom/picom.conf ~/.config/picom/
mkdir -p ~/.config/alacritty
cp ~/dotfiles/.config/alacritty/alacritty.toml ~/.config/alacritty/alacritty.toml
}

## Install Pip Dependencies

pip3 install -r pip.txt --break-system-packages