############################################################
# Dockerfile to run openmtc zigbeeipe binary
############################################################

# Set the base image to use
FROM ubuntu:16.04

# Set the file maintainer
MAINTAINER v.gowtham@tu-berlin.de


# Update the repository sources list
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip

# install packages and clean up
RUN printf "Starting update...\n" && \
    apt-get update -qq && \
    printf "Update finished.\n" && \
    printf "Starting dist-upgrade...\n" && \
    apt-get dist-upgrade -y > /dev/null && \
    printf "Upgrade finished.\n" && \
    printf "Starting install...\n" && \
    apt-get install -y \
    build-essential \
    netbase \
    iproute2 \
    python-pip \
    python-dev \
    jq > /dev/null && \
    apt-get clean && \
    printf "Installation and cleanup finished.\n"


# Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt



# Expose the default port
EXPOSE 5050

#create default directory
RUN mkdir -p /var/log/eds

ADD . /eds
# entry point
#ENTRYPOINT ["/bin/sh"]

CMD [""]

