#!/bin/bash
sudo apt install python3
sudo apt install python3-pip
sudo python3 -m pip install -r requirements.txt
clear
echo "Done!"
echo "Now run build-binaries.sh. (Skip if you want to use pre-built binary, run create-command.sh in this case)"
