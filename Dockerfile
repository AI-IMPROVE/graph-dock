
FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

LABEL MAINTAINER="wilke"
LABEL VERSION="v0.0.1"

ENV MODEL="graph-dock"
ENV CANDLE_DATA_DIR="/candle_data_dir"


RUN apt-get update -y && apt-get install -y gcc git gnupg2 vim g++ build-essential
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F60F4B3D7FA2AF80 
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC 
RUN apt-get update
RUN apt install -y build-essential g++

WORKDIR /usr/local/graph-dock
COPY . .

    
    # # install gpu fix and clean up
    # cd $SINGULARITY_ROOTFS/
    # chmod a+x singularity_gpu_fix.sh
    # ./singularity_gpu_fix.sh
    # rm ./singularity_gpu_fix.sh

    # # create default internal candle_data_dir, map external candle_data_dir here
    # mkdir -p /candle_data_dir

    # # install packages
    # # apt-get install -y git vim

    # # install python modules and model prerequisites 
    # pip install git+https://github.com/ECP-CANDLE/candle_lib@develop

    # cd /usr/local
    # git clone https://github.com/AI-IMPROVE/graph-dock.git
    # cd graph-dock
    # git checkout develop
    # pip install -r requirements.txt

    # # cp Pilot1/ST1/preprocess.sh /usr/local/bin/
    # # cp Pilot1/ST1/train.sh /usr/local/bin/
    # # cp Pilot1/ST1/infer.sh /usr/local/bin/

    # # chmod +x /usr/local/bin/preprocess.sh
    # # chmod +x /usr/local/bin/train.shh
    # # chmod +x /usr/local/bin/infer.sh