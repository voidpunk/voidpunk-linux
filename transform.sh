#!/bin/bash
echo "Updating the system..."
sudo pacman -Syu --noconfirm
echo "Adding the repo..."
sudo pacman -S --needed python
sudo python add_repo.py
echo "Creating the back of ~/.config folder..."
cp -r ~/.config ~/.config-backup
echo "Installing the packages (dependencies, utilities, themes, fonts)..."
sudo pacman -S --noconfirm --needed paru
sudo paru -S --noconfirm --needed - < pkglist.txt
python main.py