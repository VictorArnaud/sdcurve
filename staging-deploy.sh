#!/bin/bash
#
# Purpose: Continuous deploy on staging enviroment
#
# Author: Victor Arnaud <victorhad@gmail.com>
# Author: João Pedro Sconetto <sconetto.joao@gmail.com>

echo $DOCKER_HUB_PASS | docker login -username $DOCKER_HUB_USER --password-stdin
docker-compose build
docker-compose push

sudo apt-get install sshpass -y
sshpass -p $SSH_PASSWORD ssh drdown@104.236.68.6 '/bin/bash /home/drdown/sdcurve-deploy.sh'
