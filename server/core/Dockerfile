FROM python:3.8-buster
ARG DEBIAN_FRONTEND=noninteractive

#ENV DOCKERIZE_VERSION v0.2.0
#RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# App directory
WORKDIR /usr/src/app
COPY src .
# COPY ./requirements.txt /tmp/requirements.txt

RUN ["ln", "-sf", "/usr/share/zoneinfo/Asia/Seoul", "/etc/localtime"]

# RUN ["pip", "install", "-r", "/tmp/requirements.txt"]

# RUN Python
CMD ["python3", "app.py"]