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
        xdpyinfo
        python3-iwlib

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

## Copy all Dots

function copy_dots(){
    cp -r ~/dotfiles/.cache/* ~/.cache/
  mkdir -p ~/.config/alacritty
  cp ~/dotfiles/.config/alacritty/alacritty.toml ~/.config/alacritty/alacritty.toml
  cp ~/dotfiles/.shortcuts ~/
  mkdir -p ~/.config/wal/templates
  cp ~/dotfiles/.config/flameshot/flameshot.ini ~/.config/wal/templates
  mkdir -p ~/.config/dunst
  cp ~/dotfiles/.config/dunst/dunstrc ~/.config/wal/templates
  cp ~/dotfiles/.config/rofi/SpectrumOS.rasi ~/.config/wal/templates
  mkdir -p ~/.config/cava
  cp ~/dotfiles/.config/cava/config ~/.config/wal/templates
  mkdir -p ~/.config/conky
  cp ~/dotfiles/.config/conky/* ~/.config/conky/
  mkdir -p ~/.config/caffeine
  cp ~/dotfiles/.config/caffeine/* ~/.config/caffeine/
  mkdir -p ~/.config/ncspot
  cp ~/dotfiles/.config/ncspot/config.toml ~/.config/ncspot/config.toml
  mkdir -p  ~/.fonts
  cp ~/dotfiles/.fonts/* ~/.fonts
  cp ~/dotfiles/.config/gromit-mpx.cfg ~/.config/
  mkdir -p ~/.config/picom
  cp ~/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
  mkdir -p ~/.config/qtile
  cp -r ~/dotfiles/.config/qtile/* ~/.config/qtile/
  mkdir -p ~/.config/nvim
  cp -r ~/dotfiles/.config/nvim/init.vim ~/.config/nvim/
  mkdir -p ~/.config/ranger
  cp ~/dotfiles/.config/ranger/rc.conf ~/.config/ranger/rc.conf
  mkdir -p ~/.config/flameshot
  mkdir -p ~/.config/xsettingsd
  cp ~/dotfiles/.config/xsettingsd/xsettingsd.conf ~/.config/xsettingsd/xsettingsd.conf
  mkdir -p ~/.config/rofi
  cp -r ~/dotfiles/.config/rofi/* ~/.config/rofi/
  sudo mkdir -p /root/.config/rofi
  sudo cp -r ~/dotfiles/.config/rofi/* /root/.config/rofi/
  sudo mkdir -p /root/.cache/wal
  sudo mkdir -p /root/.fonts
  sudo cp -r ~/.cache/wal/colors-rofi-dark.rasi /root/.cache/wal/
  sudo timedatectl set-ntp true
  xdg-settings set default-web-browser firefox.desktop 
  mkdir -p ~/.local/bin
  cp -r ~/dotfiles/.local/bin/* ~/.local/bin
  chmod +x ~/.local/bin/*
  mkdir -p ~/.config/neofetch
  cp ~/dotfiles/.config/neofetch/config.conf ~/.config/neofetch/config.conf 
  cp ~/dotfiles/.zshrc ~/
  mkdir -p ~/.oh-my-zsh
  cp ~/dotfiles/.oh-my-zsh/themes/* ~/.oh-my-zsh/themes/
  sudo mkdir -p /usr/share/backgrounds
  mkdir -p ~/Pictures/Wallpapers
  cp -r ~/dotfiles/Wallpapers/* ~/Pictures/Wallpapers
  sudo cp ~/dotfiles/Wallpapers/wall.png /usr/local/backgrounds/background.png
  sudo mkdir -p /usr/local/themes
  sudo cp -r ~/.local/share/themes/FlatColor /usr/local/themes
  sudo chown -R $USER:$USER /usr/local/themes/FlatColor
  sudo ln -s /usr/local/themes/FlatColor /usr/share/themes/FlatColor
  sudo mkdir /usr/local/backgrounds
  sudo chown -R $USER:$USER /usr/local/backgrounds
  sudo cp ~/dotfiles/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf
  sudo cp ~/dotfiles/pulse/system.pa /etc/pulse/system.pa
  sudo cp ~/dotfiles/touchpad/30-touchpad.conf /etc/X11/xorg.conf.d/
  mkdir -p ~/notable
  mkdir -p ~/book
  mkdir -p ~/Articles
}

## Install Pip Dependencies

#pip3 install -r pip.txt --break-system-packages

copy_dots