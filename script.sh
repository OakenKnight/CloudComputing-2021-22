#!/bin/bash

echo "Starting to set custom environment variables..."
echo "Creating custom file to add environment variables..."
sudo touch /etc/profile.d/custom.sh
echo "Granting permissions to file for user vagrant..."
sudo chown vagrant: /etc/profile.d/custom.sh
echo "Adding environment variables..."
sudo echo export DB_USERNAME="postgres" >> /etc/profile.d/custom.sh
sudo echo export DB_PASSWORD="postgres" >> /etc/profile.d/custom.sh
sudo echo export DB_NAME="cloudv2" >> /etc/profile.d/custom.sh
sudo echo export DB_PORT="5432" >> /etc/profile.d/custom.sh
sudo echo export DB_HOST="localhost" >> /etc/profile.d/custom.sh

echo "Custom environment variables all set!"