#!/bin/bash

echo -e "\033[0;32m====================================="
echo -e "\033[1;32mThe Linux IT Guy - EndeavourOS Scripts"
echo -e "\033[1;32mRemoving Lutris"
echo -e "\033[0;32m=====================================\033[0m"

# Remove Lutris
flatpak uninstall -y flathub net.lutris.Lutris
