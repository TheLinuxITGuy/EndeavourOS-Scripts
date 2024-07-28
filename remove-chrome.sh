#!/bin/bash

APP_NAME="google-chrome"

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
