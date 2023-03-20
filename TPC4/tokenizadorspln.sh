#!/bin/bash

chmod +x tokenizadorSPLN
sudo cp tokenizadorSPLN /usr/local/bin
export PATH="$PATH:$HOME/usr/local/bin"
source ~/.bashrc