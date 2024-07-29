#!/bin/bash

APP_NAME="brave-bin"

echo -e "\033[0;32m====================================="
echo -e "\033[1;32mThe Linux IT Guy - EndeavourOS Scripts"
echo -e "\033[1;32mRemoving $APP_NAME"
echo -e "\033[0;32m=====================================\033[0m"

#Check if yay is installed
if ! command -v yay &>/dev/null
then
    echo "yay is not installed. Please install yay first."
    exit 1
fi

# Check if the app is installed
if yay -Q $APP_NAME &> /dev/null
then
    echo "$APP_NAME is installed. Removing now..."
    # Remove the app
    yay -R --noconfirm $APP_NAME
else
    echo "$APP_NAME is not installed. Skipping removal."
fi
