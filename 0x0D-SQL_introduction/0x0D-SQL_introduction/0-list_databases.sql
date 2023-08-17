#!/bin/bash

# MySQL server connection details
MYSQL_USER="root"
MYSQL_PASSWORD="your_mysql_password"
MYSQL_HOST="localhost"

# Execute the command to list databases
mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -h$MYSQL_HOST -e "SHOW DATABASES;"
