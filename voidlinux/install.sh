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
        'xorg-minimal'
        'xorg-fonts'
        'xinit'
        'elogind'
        'dbus-elogind'
        'polkit'
        'qtile'
        'python3-qtile-extras'
        'alacritty'
        'vim'
        'xf86-video-vmware' # Use Correct for Video Card
        'git'
        'curl'
        'zsh'
        'thefuck'
        'pywal'
        'setxkbmap'
        'bc'
        'picom'
        'iproute2'
        'inetutils'
        'xdpyinfo'
        'python3-iwlib'
        'python3-dateutil'
        'python3-xdg'
        'cava'
        'pulseaudio'
        'pavucontrol'
        'arandr'
        'rofi'
        'vscode'
        'htop'
        'feh'
        'unclutter'
        'fuse-exfat'
        'openssh'
        'xcolor'
        'playerctl'
        'scrot'
        'flameshot'
        'python3-pip'
        'ranger'
        'lxappearance'
        'acpilight'
        'alsa-utils'
        'surfraw'
        'bmon'
        'lm_sensors'
        'ueberzug'
        'tk'
        'dunst'
        'xsettingsd'
        'transmission'
        'vlc'
        'kdeconnect'
        'lightdm-webkit2-greeter'
        'rsync'
        'cmus'
        'xdg-user-dirs'
        'neofetch'
        'firefox'
        'xkill'
        'bluez'
        'bluez-alsa'
        'ripgrep'
        'blueman'
        'jp2a'
        'os-prober'
        'gnome-disk-utility'
        'NetworkManager'
        'tlp'
        'gvfs'
        'barrier'
        'noto-fonts-ttf'
        'noto-fonts-cjk'
        'noto-fonts-emoji'
        'tumbler'
        'redshift'
        'neovim'
        'libmicrodns'
        'protobuf'
        'pamixer'
        'gvfs-mtp'
        'gvfs-smb'
        'exa'
        'xclip'
        'xdotool'
        'nvidia-dkms'
        'cups'
        'cups-pdf'
        'avahi'
        'caffeine-ng'
        'telegram-desktop'
        'chromium'
        'wpgtk'
        'thunar'
        'thunar-volman'
        'thunar-archive-plugin'
        'thunar-media-tags-plugin'
        'hugo'
        'gromit-mpx'
        'ntfs-3g'
        'i3lock-color'
        'i3lock-fancy'
        'lazydocker'
        'rofi-emoji'
        'psmisc'
        'lightdm'
        'lightdm-gtk-greeter'
        'meson'
        'ninja'
        'gcc'
        'make'
        'pkg-config'
        'xorgproto'
        'pcre'
        'pcre-devel'
        'xcb-util-image'
        'xcb-util-renderutil'
        'xcb-util-wm'
        'libev'
        'libxdg-basedir'
        'libconfig'
        'libev-devel'
        'pixman'
        'pixman-devel'
        'libX11'
        'libX11-devel'
        'xcb-util-image-devel'
        'xcb-util-renderutil-devel'
        'libXext'
        'libXext-devel'
        'pcre2'
        'pcre2-devel'
        'libepoxy'
        'libepoxy-devel'
        'dbus-devel'
        'libconfig-devel'
        'glib'
        'glib-devel'
        'cairo'
        'cairo-devel'
        'rofi-devel'
        'uthash-devel'
    )
for packet in "${packets[@]}"; do
    sudo xbps-install -Sy "${packet}"
done

function zsh_install(){
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
    chsh -s $(which zsh)
}

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

## Install Lightdm

function lightdm_install(){

sudo cp ~/dotfiles/lightdm/lightdm.conf
sudo cp ~/dotfiles/lightdm/lightdm-webkit2-greeter.conf
sudo cp -r ~/dotfiles/lightdm/theme/SpectrumOS /usr/share/lightdm-webkit/themes/

sudo ln -s /etc/sv/lightdm /var/service/
sudo ln -s /etc/sv/dbus /var/service/
sudo ln -s /etc/sv/elogind /var/service/
}

## install picom

function install_picom(){
    git clone https://github.com/FT-Labs/picom.git
    cd picom
    meson --buildtype=release . build
    ninja -C build
    sudo ninja -C build install
}

## install rofi extended

function install_rofi_extended(){
    git clone https://github.com:marvinkreis/rofi-file-browser-extended.git
    cd rofi-file-browser-extended
    cmake .
    make
    sudo make installE
}

## install farge

function install_farge(){
    git clone https://github.com:sdushantha/farge.git
    cd farge
    sudo make install
}



## Actualizar Grub

function grubup(){
# Archivo de configuración de GRUB
GRUB_CONFIG="/etc/default/grub"

# Imagen de fondo para GRUB
BACKGROUND_IMAGE="/usr/local/backgrounds/background.png"

# Verificar si el archivo de configuración de GRUB existe
if [ -f "$GRUB_CONFIG" ]; then
    # Asegurarse de que la imagen de fondo tenga permisos correctos
    sudo chmod +r $BACKGROUND_IMAGE

    # Agregar o modificar las líneas necesarias en el archivo de configuración de GRUB

    # Agregar o modificar la línea GRUB_CMDLINE_LINUX_DEFAULT
    if grep -q "^GRUB_CMDLINE_LINUX_DEFAULT" "$GRUB_CONFIG"; then
        sudo sed -i 's/^GRUB_CMDLINE_LINUX_DEFAULT="\(.*\)"/GRUB_CMDLINE_LINUX_DEFAULT="\1 quiet splash"/' "$GRUB_CONFIG"
    else
        echo 'GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"' | sudo tee -a "$GRUB_CONFIG"
    fi

    # Agregar o modificar la línea GRUB_GFXMODE
    if grep -q "^GRUB_GFXMODE" "$GRUB_CONFIG"; then
        sudo sed -i 's/^GRUB_GFXMODE=.*/GRUB_GFXMODE=auto/' "$GRUB_CONFIG"
    else
        echo 'GRUB_GFXMODE=auto' | sudo tee -a "$GRUB_CONFIG"
    fi

    # Agregar o modificar la línea GRUB_BACKGROUND
    if grep -q "^GRUB_BACKGROUND" "$GRUB_CONFIG"; then
        sudo sed -i "s|^GRUB_BACKGROUND=.*|GRUB_BACKGROUND=\"$BACKGROUND_IMAGE\"|" "$GRUB_CONFIG"
    else
        echo "GRUB_BACKGROUND=\"$BACKGROUND_IMAGE\"" | sudo tee -a "$GRUB_CONFIG"
    fi

    # Agregar o modificar la línea GRUB_TERMINAL_OUTPUT
    if grep -q "^GRUB_TERMINAL_OUTPUT" "$GRUB_CONFIG"; then
        sudo sed -i 's/^GRUB_TERMINAL_OUTPUT=.*/GRUB_TERMINAL_OUTPUT=gfxterm/' "$GRUB_CONFIG"
    else
        echo 'GRUB_TERMINAL_OUTPUT=gfxterm' | sudo tee -a "$GRUB_CONFIG"
    fi

    # Actualizar la configuración de GRUB
    sudo update-grub

    echo "Configuración de GRUB actualizada correctamente."
else
    echo "El archivo de configuración de GRUB no existe: $GRUB_CONFIG"
    exit 1
fi

}


## Install Plymouth

function plymouth_install(){
sudo xbps-install -S plymouth

sudo cp -r ~/dotfiles/plymouth/themes/spectrumos /usr/share/plymouth/themes/
sudo plymouth-set-default-theme -R spectrumos
sudo dracut --force

GRUB_CONFIG="/etc/default/grub"
GRUB_CMDLINE="quiet splash"

sudo update-grub
sudo ln -s /etc/sv/plymouth /var/service/
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
  fc-cache -fv
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

function qtilebonsai(){
    git clone https://github.com/aravinda0/qtile-bonsai.git
    cd qtile-bonsai
    pip3 install . --break-system-packages
}

function post(){
    sudo ln -s /etc/sv/bluetoothd /var/service/
    sudo sv start bluetoothd
    sudo ln -s /etc/sv/tlp /var/service/
    sudo sv start tlp
    wpg-install -gio
}

## Install Pip Dependencies
#base_install
#pip3 install -r pip.txt --break-system-packages
#qtile_install
#qtilebonsai
zsh_install
#lightdm_install
install_picom
#install_rofi_extended
#install_farge
#grubup
#plymouth_install
#copy_dots