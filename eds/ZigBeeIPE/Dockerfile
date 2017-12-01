############################################################
# Dockerfile to run openmtc zigbeeipe binary
############################################################

# Set the base image to use
FROM ubuntu:16.04

# Set the file maintainer
MAINTAINER {sathi,v.gowtham}@tu-berlin.de

# Update the repository sources list
RUN apt-get update

WORKDIR /home/elastest/eds/ZigBeeIPE
ADD . /home/elastest/eds/ZigBeeIPE

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
    libev-dev \
    gcc \
    make \
    automake \
    jq > /dev/null && \
    apt-get clean && \
    printf "Installation and cleanup finished.\n"



# Install any needed packages specified in dependencies.txt
RUN pip install -r openmtc-gevent/dependencies.txt
ADD setup-sdk.py /
RUN python setup-sdk.py install


# Expose the default port
EXPOSE 5001

#create default directory
RUN mkdir -p /var/log/eds
RUN chmod +x /var/log/eds

# entry point
ENTRYPOINT ["/bin/sh",  "/home/elastest/eds/ZigBeeIPE/exec-zigbeeipe.sh"]
