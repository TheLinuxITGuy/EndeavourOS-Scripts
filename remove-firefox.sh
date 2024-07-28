#!/bin/bash

APP_NAME="firefox"

# Check if the app is already installed
if command -v $APP_NAME &> /dev/null
then
    echo "$APP_NAME is installed. Removing now..."
    # Remove the app
    sudo pacman -R --noconfirm $APP_NAME
else
    echo "$APP_NAME is not installed. Skipping removal."
fi
