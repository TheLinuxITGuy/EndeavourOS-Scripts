#!/bin/bash

APP_NAME="steam"
APP2_NAME="protonup-qt"

echo -e "\033[0;32m====================================="
echo -e "\033[1;32mThe Linux IT Guy - EndeavourOS Scripts"
echo -e "\033[1;32mRemoving $APP_NAME and $APP2_NAME"
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

#Check if yay is installed
if ! command -v yay &>/dev/null
then
    echo "yay is not installed. Please install yay first."
    exit 1
fi

# Check if the app is installed
if yay -Q $APP2_NAME &> /dev/null
then
    echo "$APP_NAME is installed. Removing now..."
    # Remove the app
    yay -R --noconfirm $APP2_NAME
else
    echo "$APP2_NAME is not installed. Skipping removal."
fi
