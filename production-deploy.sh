#!/bin/bash
#
# Purpose: Continuous deploy on production enviroment
#
# Author: Victor Arnaud <victorhad@gmail.com>
# Author: João Pedro Sconetto <sconetto.joao@gmail.com>

echo $DOCKER_HUB_PASS | docker login -username $DOCKER_HUB_USER --password-stdin
python3 manage.py collectstatic
docker-compose -f docker-compose.production.yml build
docker-compose -f docker-compose.production.yml push

sudo apt-get install sshpass -y
sshpass -p $SSH_PASSWORD ssh drdown@159.203.182.32 '/bin/bash /home/drdown/sdcurve-deploy.sh'
