#!/bin/bash

sudo systemctl start bluetooth # to start it for the session will stay disabled after reboot.

sudo systemctl enable bluetooth # to enable per default, will run after every boot.

# https://discovery.endeavouros.com/audio/bluetooth/2021/03/
