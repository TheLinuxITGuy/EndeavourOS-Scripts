#!/bin/bash

echo -e "\033[0;32m====================================="
echo -e "\033[1;32mThe Linux IT Guy - EndeavourOS Scripts"
echo -e "\033[1;32mDisabling Bluetooth"
echo -e "\033[0;32m=====================================\033[0m"

sudo systemctl stop bluetooth # to stop it for the session will stay enabled after reboot.

sudo systemctl disable bluetooth # to disable per default, will run after every boot.

# https://discovery.endeavouros.com/audio/bluetooth/2021/03/
