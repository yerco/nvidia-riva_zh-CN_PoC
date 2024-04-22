#!/bin/bash

# Run as sudo
# Requires sudo apt-get install expect 

# Check if the correct number of arguments were provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <API_KEY> <ORG>"
    exit 1
fi

# Arguments to provide
API_KEY=$1
ORG=$2

yes "y" | /opt/ngc-cli/ngc version upgrade

./configure_ngc.exp "$API_KEY" "$ORG"

echo "NGC configured.\n\n\n"

chmod -R go+rx /opt/ngc-cli

apt-get update

apt-get install -y apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

apt-get update

yes "" | apt-get install -y nvidia-docker2

echo "nvidia-docker2 installed"

#./install_nvidia_docker.exp

systemctl restart docker

docker run --rm --gpus all nvidia/cuda:11.0.3-base nvidia-smi

./docker_login_ngc.exp

echo "PULLING..."

docker pull nvcr.io/nvidia/riva/riva-speech:2.15.0-servicemaker

/opt/ngc-cli/ngc registry resource download-version "nvidia/riva/riva_quickstart:2.15.0"

chmod a+rwx /home/ubuntu/riva_quickstart_v2.15.0/
#cd /home/ubuntu/riva_quickstart_v2.15.0/

chmod ugo+rx *

yes "y" | /opt/miniconda/condabin/conda create --name=tresdiez python=3.10

/opt/miniconda/condabin/conda activate tres-diez

# here it comes the riva_init.sh and riva_start.sh using a custom config.sh
