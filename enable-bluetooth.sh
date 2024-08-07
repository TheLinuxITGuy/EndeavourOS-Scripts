#!/bin/bash

echo -e "\033[0;32m====================================="
echo -e "\033[1;32mThe Linux IT Guy - EndeavourOS Scripts"
echo -e "\033[1;32mEnabling Bluetooth"
echo -e "\033[0;32m=====================================\033[0m"

sudo systemctl start bluetooth # to start it for the session will stay disabled after reboot.

sudo systemctl enable bluetooth # to enable per default, will run after every boot.

# https://discovery.endeavouros.com/audio/bluetooth/2021/03/
