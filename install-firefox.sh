#!/bin/bash

APP_NAME="firefox"

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
