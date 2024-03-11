# Brian Joseph Lesko
# Robotics and Computer Engineering

# This is a dockerfile that is used to create a docker image, which runs a container that hosts a MySQL database server.

# to build this image run "docker build -t my-custom-mysql ."
# check if the build was proper with "docker images"
# to run the container use "docker run -d -p 3306:3306 --name my-mysql my-custom-mysql"
# note, we must specify the port to be exposed in the run line again, but not the root password

# Use the latest stable version of MySQL compatible with Ubuntu 22.04
FROM mysql:latest

# Set the environment variable for the MySQL root password
ENV MYSQL_ROOT_PASSWORD=lesko

# Expose port 3306
EXPOSE 3306

# MySQL uses /var/lib/mysql for its data directory
VOLUME /var/lib/mysql
