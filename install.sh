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
function base() {
  packets=(
    'feh'
    'unclutter'
    'fuse-exfat'
    'base-devel'
    'alsa-utils'
    'pulseaudio-alsa'
    'pavucontrol'
    'openssh'
    'alacritty'
    'xcolor'
    'playerctl'
    'scrot'
    'flameshot'
    'rofi'
    'surfraw'
    'python-pip'
    'ranger'
    'lxappearance'
    'bmon'
    'acpilight'
    'lm_sensors'
    'nm-connection-editor'
    'arandr'
    'python-psutil'
    'python-xdg'
    'python-iwlib'
    'python-dateutil'
    'ueberzug'
    'xsettingsd'
    'zsh'
    'dunst'
    'tk'
    'transmission-cli'
    'vlc'
    'kdeconnect'
    'lightdm-gtk-greeter-settings'
    'reflector'
    'rsync'
    'curl'
    'cmus'
    'bc'
    'neofetch'
    'firefox'
    'cmus'
    'xorg-xkill'
    'xdg-user-dirs'
    'bluez'
    'bluez-tools'
    'bluez-utils'
    'ripgrep'
    'blueman'
    'htop'
    'jp2a'
    'locate'
    'os-prober'
    'gnome-disk-utility'
    'networkmanager'
    'unzip'
    'xarchiver'
    'tlp'
    'gvfs'
    'barrier'
    'noto-fonts'
    'noto-fonts-cjk'
    'noto-fonts-emoji'
    'ttf-dejavu'
    'ttf-liberation'
    'ttf-opensans'
    'libayatana-appindicator'
    'tlp'
    'powertop'
    'tumbler'
    'redshift'
    'libmicrodns' # Libraries for vlc and Chromecast
    'protobuf' # Libraries for vlc and Chromecast
    #'linux'
    #'linux-headers'
    #'linux-docs'
    'linux-lts'
    'linux-lts-headers'
    'linux-lts-docs'
    #'linux-zen-headers'
    #'linux-zen-docs'
    'neovim'
    'xorg-xdpyinfo'
    #'taskwarrior-tui'
    'fd'
    'fzf'
    'cups'
    'thefuck'
    'pamixer'
    'gvfs-mtp' 
    'gvfs-nfs'
    'gvfs-smb'
    'exa'
    'xclip'
    'xdotool'
    #'nvidia-dkms'
    'cups'
    'cups-pdf'
    'man'
    'avahi'
    #'zxel' # Needed for Calculator
)

for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    sudo pacman -S "${packet}" --noconfirm --needed
done
}

function paru_install(){
  git clone https://aur.archlinux.org/paru.git 
  cd paru 
  makepkg -si --noconfirm
  cd ..
  rm -rf paru
} 

function aur_packages() {
  packets=(
    #'qtile-git'
    'farge'
    #'python-pywalfox' # If you install firefox you will need  this
    'qtile-extras-git'
    'caffeine-ng-git'
    'visual-studio-code-bin'
    'pulseaudio-bluethooth'
    'telegram-desktop'
    'google-chrome'
    'wpgtk-git'
    'insect'
    'cava-git'
    'thunar-extended'
    'thunar-volman'
    'hugo'
    'gromit-mpx-git'
    'nbfc'
    'ntfs-3g'
    'i3lock-color'
    'i3lock-fancy-git'
    'wal-telegram-git'
    'picom-tyrone-git'
    'lazy-docker'
    'rofi-emoji'
    'zathura-pdf-mupdf' 
    'zathura-pywal-git'
    'zathura-ps'
    'libby-git'
    'python-rofi-git' 
    'lyrics-in-terminal'
    'picom-ftlabs-git'
    'ncspot'
    'rofi-file-browser-extended-git'
    'ttf-courier-prime'

)
for packet in "${packets[@]}"; do
    echo "Instalando --> ${packet}"
    paru -S "${packet}" --noconfirm
done
}

function zsh(){
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
}

function copy_dotfiles(){
  wpg-install.sh -gio
  cp -r ~/SpectrumOS/dotfiles/.cache/* ~/.cache/
  mkdir -p ~/.config/alacritty
  cp ~/SpectrumOS/dotfiles/.config/alacritty/alacritty.toml ~/.config/alacritty/alacritty.toml
  cp ~/SpectrumOS/dotfiles/.shortcuts ~/
  mkdir -p ~/.config/wal/templates
  
  mkdir -p ~/.config/dunst
  cp ~/SpectrumOS/dotfiles/.config/dunst/dunstrc ~/.config/wal/templates
  cp ~/SpectrumOS/dotfiles/.config/rofi/SpectrumOS.rasi ~/.config/wal/templates
  mkdir -p ~/.config/cava
  cp ~/SpectrumOS/dotfiles/.config/cava/config ~/.config/wal/templates
  mkdir -p ~/.config/conky
  cp ~/SpectrumOS/dotfiles/.config/conky/* ~/.config/conky/
  mkdir -p ~/.config/caffeine
  cp ~/SpectrumOS/dotfiles/.config/caffeine/* ~/.config/caffeine/
  mkdir -p ~/.config/ncspot
  cp ~/SpectrumOS/dotfiles/.config/ncspot/config.toml ~/.config/ncspot/config.toml
  mkdir -p  ~/.fonts
  cp ~/SpectrumOS/dotfiles/.fonts/* ~/.fonts
  cp ~/SpectrumOS/dotfiles/.config/gromit-mpx.ini ~/.config
  mkdir -p ~/.config/picom
  cp ~/SpectrumOS/dotfiles/.config/picom/picom.conf ~/.config/picom/picom.conf
  mkdir -p ~/.config/qtile
  cp -r ~/SpectrumOS/dotfiles/.config/qtile/* ~/.config/qtile/
  mkdir -p ~/.config/nvim
  cp -r ~/SpectrumOS/dotfiles/.config/nvim/init.vim ~/.config/nvim/
  mkdir -p ~/.config/ranger
  cp ~/SpectrumOS/dotfiles/.config/ranger/rc.conf ~/.config/ranger/rc.conf
  mkdir -p ~/.config/xsettingsd
  cp ~/SpectrumOS/dotfiles/.config/xsettingsd/xsettingsd.conf ~/.config/xsettingsd/xsettingsd.conf
  mkdir -p ~/.config/rofi
  cp -r ~/SpectrumOS/dotfiles/.config/rofi/* ~/.config/rofi/
  sudo mkdir -p /root/.config/rofi
  sudo cp -r ~/SpectrumOS/dotfiles/.config/rofi/* /root/.config/rofi/
  sudo mkdir -p /root/.cache/wal
  sudo mkdir -p /root/.fonts
  sudo cp -r ~/.cache/wal/colors-rofi-dark.rasi /root/.cache/wal/
  sudo timedatectl set-ntp true
  xdg-settings set default-web-browser firefox.desktop 
  mkdir -p ~/.local/bin
  cp -r ~/SpectrumOS/dotfiles/.local/bin/* ~/.local/bin
  chmod +x ~/.local/bin/*
  mkdir -p ~/.config/neofetch
  cp ~/SpectrumOS/dotfiles/.config/neofetch/config.conf ~/.config/neofetch/config.conf 
  cp ~/SpectrumOS/dotfiles/.zshrc ~/
  mkdir -p ~/.oh-my-zsh
  cp ~/SpectrumOS/dotfiles/.oh-my-zsh/themes/* ~/.oh-my-zsh/themes/
  mkdir ~/Pictures
  sudo mkdir -p /usr/share/backgrounds
  mkdir -p ~/Pictures/Wallpapers
  cp -r ~/SpectrumOS/Wallpapers/* ~/Pictures/Wallpapers
  sudo cp ~/SpectrumOS/dotfiles/Wallpapers/wall.png /usr/local/backgrounds/background.png
  sudo mkdir -p /usr/local/themes
  sudo cp -r ~/.local/share/themes/FlatColor /usr/local/themes
  sudo chown -R $USER:$USER /usr/local/themes/FlatColor
  sudo ln -s /usr/local/themes/FlatColor /usr/share/themes/FlatColor
  sudo mkdir /usr/local/backgrounds
  sudo chown -R $USER:$USER /usr/local/backgrounds
  sudo cp ~/SpectrumOS/dotfiles/lightdm/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf
  sudo cp ~/SpectrumOS/dotfiles/pulse/system.pa /etc/pulse/system.pa
  mkdir -p ~/notable
  mkdir -p ~/book
  mkdir -p ~/Articles
}

function lqx(){
  curl -s 'https://liquorix.net/install-liquorix.sh' | sudo bash
}

function copy_dots(){
  wpg-install.sh -gio
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

function web_apps(){
  mkdir -p ~/Apps
  cd ~/Apps
  nativefier https://github.com/ --name github --single-instance 
  nativefier https://www.primevideo.com/ --name prime --single-instance --windevine 
  nativefier https://drive.google.com/drive/shared-drives --name drive --single-instance 
  nativefier https://www.figma.com/files/recent?fuid=1177005402390460721 --name figma --single-instance 
  nativefier https://admin.google.com/?rapt=AEjHL4N0yGwzCoucouWtW0MKQj6kYhIIfkadjCaxgZTjhnUCSuKHDVoVPYARCWt1YOfZ542j11diwR4Td8HEVfzHv_vT509KMg --name admin --single-instance 
  nativefier https://calendar.google.com/calendar/u/0/r?pli=1 --name calendar --single-instance 
  nativefier https://www.notion.so/helgen/00-Helgen-Ltd-42570ee0ace34d19b7d0a91955b7d976--name notion --single-instance 
  nativefier https://www.overleaf.com/project --name overleaf --single-instance 
  nativefier https://meet.google.com/ --name meet --single-instance 
  nativefier https://app.clockify.me/tracker# --name clockify --single-instance 
  nativefier https://admin.microsoft.com/Adminportal/Home#/homepage --name madmin --single-instance
  nativefier https://helgentrial.atlassian.net/jira/software/projects/IR/boards/1 --name jira --single-instance

  nativefier https://search.brave.com/ --name search --single-instance --clear-cache --user-agent 'firefox' --show-menu-bar --bookmarks-menu
  sudo ln -s ~/Apps/PrimeVideo/WelcometoPrimeVideo /usr/bin/prime
  sudo ln -s ~/Apps/drive/drive /usr/bin/drive
  sudo ln -s ~/Apps/admin/admin /usr/bin/admin
  sudo ln -s ~/Apps/calendar/calendar /usr/bin/calendar
  sudo ln -s ~/Apps/notion/notion /usr/bin/notion
  sudo ln -s ~/Apps/overleaf/overleaf /usr/bin/overleaf
  sudo ln -s ~/Apps/figma/figma /usr/bin/figma
  sudo ln -s ~/Apps/meet/meet /usr/bin/meet
  sudo ln -s ~/Apps/github/github /usr/bin/github
  sudo ln -s ~/Apps/clockify/clockify /usr/bin/clockify
   sudo ln -s ~/Apps/jira/jira /usr/bin/jira

}

function post(){
  sudo usermod -aG network $USER
  wal -i ~/Pictures/Wallpapers/wall.png
  fc-cache -f -v
  timedatectl set-timezone America/Mexico_City
  sudo systemctl enable bluetooth.service
  sudo systemctl start bluetooth.service
  sudo systemctl enable sshd.service
  sudo systemctl start sshd.service
  sudo systemctl enable tlp.service
  journalctl --vacuum-size=100M
  journalctl --vacuum-time=2weeks
  timedatectl set-local-rtc 1
  
}

function install_docker(){
  sudo pacman -S docker docker-buildx docker-compose --noconfirm --needed
  sudo systemctl enable docker.service
  sudo systemctl start docker.service
  sudo usermod -aG docker $USER
}

function neovim(){
  curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
}

# sudo pacman -Syyu --noconfirm
# sudo pacman -Rcns qtile --noconfirm
#base
#paru_install
#aur_packages
#pip install -r pip.txt --break-system-packages
#zsh
#lqx
#copy_dotfiles
#copy_dots
#post
#web_apps
#update
install_docker

