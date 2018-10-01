#!/bin/bash

# Script to import set of sample bags
# Copies files to data upload directory and then runs cron

cp -r ../sample_bags/* /data/org1/upload/
chown -R admin /data/org1/upload/
python manage.py runcrons bag_transfer.lib.cron.DiscoverTransfers
