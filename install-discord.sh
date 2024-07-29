#!/bin/bash

APP_NAME="discord"

echo -e "\033[0;32m====================================="
echo -e "\033[1;32mThe Linux IT Guy - EndeavourOS Scripts"
echo -e "\033[1;32mInstalling $APP_NAME"
echo -e "\033[0;32m=====================================\033[0m"

# Check if the app is already installed
if ! command -v $APP_NAME &> /dev/null
then
    echo "$APP_NAME is not installed. Installing now..."
    # Update the package database
    sudo pacman -Sy
    # Install the app
    sudo pacman -S --noconfirm $APP_NAME
else
    echo "$APP_NAME is already installed. Skipping installation."
fi
