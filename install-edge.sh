#!/bin/bash

APP_NAME="microsoft-edge-stable-bin"

#Check if yay is installed
if ! command -v yay &>/dev/null
then
    echo "yay is not installed. Please install yay first."
    exit 1
fi

# Check if the app is already installed
if ! yay -Q $APP_NAME &> /dev/null
then
    echo "$APP_NAME is not installed. Installing now..."
    # Install the app
    yay -S --noconfirm $APP_NAME
else
    echo "$APP_NAME is already installed. Skipping installation."
fi
