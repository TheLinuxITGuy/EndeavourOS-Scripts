#!/bin/bash

APP_NAME="obs-studio"

echo -e "\033[0;32m====================================="
echo -e "\033[1;32mThe Linux IT Guy - EndeavourOS Scripts"
echo -e "\033[1;32mRemoving $APP_NAME"
echo -e "\033[0;32m=====================================\033[0m"

# Check if the app is already installed
if command -v $APP_NAME &> /dev/null
then
    echo "$APP_NAME is installed. Removing now..."
    # Remove the app
    sudo pacman -R --noconfirm $APP_NAME
else
    echo "$APP_NAME is not installed. Skipping removal."
fi