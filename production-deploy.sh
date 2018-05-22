#!/bin/bash
#
# Purpose: Continuous deploy on staging enviroment
#
# Author: Victor Arnaud <victorhad@gmail.com>
# Author: João Pedro Sconetto <sconetto.joao@gmail.com>

docker tag victorhad/sdcurve:local sconetto/sdcurve
docker push sconetto/sdcurve

sudo apt-get install sshpass -y
sshpass -p $SSH_PASSWORD ssh drdown@159.203.182.32 '/bin/bash /home/drdown/sdcurve-deploy.sh'