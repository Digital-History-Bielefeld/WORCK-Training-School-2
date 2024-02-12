#!/bin/bash

# Create/Update the package lists for upgrades and new package installations
sudo apt update
# Install the `tesseract-ocr` package
sudo apt install --no-install-recommends --yes tesseract-ocr
# Cleanup
sudo rm --recursive /var/lib/apt/lists/*

echo ""
echo ""
echo ""

echo "##################################################"
echo "# Tesseract-OCR has been installed successfully. #"
echo "##################################################"
