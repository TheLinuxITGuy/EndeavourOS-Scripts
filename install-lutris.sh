#!/bin/bash

echo -e "\033[0;32m====================================="
echo -e "\033[1;32mThe Linux IT Guy - EndeavourOS Scripts"
echo -e "\033[1;32mInstalling Lutris"
echo -e "\033[0;32m=====================================\033[0m"

# Update the package list
sudo pacman -Sy

# Install flatpak
sudo pacman -S --noconfirm flatpak

# Add the Flathub repository
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Install Lutris
flatpak install -y flathub net.lutris.Lutris
