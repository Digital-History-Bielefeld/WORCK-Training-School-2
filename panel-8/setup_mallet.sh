#!/bin/bash

echo "Running setup_mallet.sh script..."
echo "Current working directory: $(pwd)"

# Install MALLET
wget http://mallet.cs.umass.edu/dist/mallet-2.0.8.zip
unzip mallet-2.0.8.zip
export PATH=$PATH:$(pwd)/panel-8/mallet-2.0.8/bin

# Clean up
rm mallet-2.0.8.zip
