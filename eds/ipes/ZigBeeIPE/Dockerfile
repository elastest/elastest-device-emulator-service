############################################################
# Dockerfile to run openmtc zigbeeipe binary
############################################################

# Set the base image to use
FROM debian:jessie


# Set the file maintainer
MAINTAINER sathi@tu-berlin.de


# Update the repository sources list
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip



# Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt



# Expose the default port
EXPOSE 5001

#create default directory
RUN mkdir -p /var/log/eds


# entry point
ENTRYPOINT ["/usr/local/bin/eds"]
CMD [""]

