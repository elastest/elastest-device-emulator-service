##############################################################################
# Dockerfile for EDS Gateway
#############################################################################

# Set the base image to use debian
FROM debian:jessie

ENV base_path=/usr/local/src
ENV openmtc_path=${base_path}/openmtc
ENV openmtc_git=https://github.com/OpenMTC/OpenMTC.git

# Set the file maintainer
MAINTAINER v.gowtham@tu-berlin.de

# Install packages and clean up
RUN printf "Starting update...\n" && \
    apt-get update -qq && \
    printf "Update finished. \n" && \
    printf "Starting dist-upgrade...\n" && \
    apt-get dist-upgrade -y > /dev/null && \
    printf "Upgrade finished. \n" && \
    printf "Starting install...\n" && \
    apt-get install -y \
    build-essential \
    netbase \
    iproute2 \
    python-pip \
    python-dev \
    curl \
    git \
    jq > /dev/null && \
    apt-get clean && \
    printf "Installation and cleanup finished.\n"

EXPOSE 8000

RUN mkdir -p ${base_path}

WORKDIR ${base_path}

RUN git clone ${openmtc_git} openmtc

WORKDIR ${openmtc_path}

RUN chmod +x create-binary-dist

RUN ./create-binary-dist gateway

RUN mkdir -p ${openmtc_path}/tmp

RUN mv dist/openmtc-all.docker.tar.gz tmp/openmtc-gateway.tar.gz

RUN python -c "from importlib import import_module;\
	       from re import sub;\
	       setup = import_module('setup-gevent-all', 'setup-gevent-all');\
	       print('\n'.join(map(lambda x: sub('[\s+]', '', x), \
               setup.SETUP_INSTALL_REQUIRES)))" > tmp/gateway-dependencies.txt

RUN cp tmp/gateway-dependencies.txt /tmp/requirements.txt

RUN pip install --upgrade --requirement /tmp/requirements.txt

RUN pip install --upgrade python-logstash

RUN cp tmp/openmtc-gateway.tar.gz /tmp/openmtc-gateway.tar.gz

RUN tar xzf /tmp/openmtc-gateway.tar.gz -C / \
    --owner root --group root --no-same-owner --no-overwrite-dir \
    --transform 's/json\.dist/json/' --show-transformed

RUN mkdir -p /var/log/openmtc

RUN cp docker/configure-gateway-and-start /usr/local/bin/configure-and-start

COPY . /tmp/
RUN cp /tmp/startup.sh ${openmtc_path}
RUN chmod +x startup.sh

ENTRYPOINT ["/usr/local/src/openmtc/startup.sh"]
CMD [""]
