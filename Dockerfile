FROM ubuntu:18.04

ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive

# Install host packages
RUN set -x \
	&& apt-get update \
	&& apt-get upgrade -y \
	&& apt-get -y install git

RUN apt-get install -y python3-pip curl libopenblas-dev python3-scipy cython libhdf5-dev python3-h5py portaudio19-dev swig libpulse-dev libatlas-base-dev
RUN pip3 install numpy==1.16
RUN pip3 install tensorflow==1.13.1
RUN pip3 install sonopy
RUN pip3 install pyaudio
RUN pip3 install keras==2.1.5
RUN pip3 install h5py
RUN pip3 install wavio
RUN pip3 install typing
RUN pip3 install prettyparse==1.1.0
RUN pip3 install attrs
RUN pip3 install fitipy==0.1.2
RUN pip3 install speechpy-fast
RUN pip3 install pyache

RUN git clone --branch dev https://github.com/MycroftAI/mycroft-precise/ /opt/precise
RUN pip3 install /opt/precise
RUN mkdir /opt/precise/training

WORKDIR /opt/precise/training

ENTRYPOINT ["/bin/bash", "/opt/precise/training/train.sh"]