FROM ubuntu
RUN apt-get update
RUN apt-get install -y git python python-pip python-dev build-essential libssl-dev

RUN pip install git+https://github.com/renyufu/restexec.git

VOLUME /wd
WORKDIR /wd

ENTRYPOINT ["restexec"]
