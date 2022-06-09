# Dockerfile for Database

FROM mariadb:10.6.4-focal
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/src/app
COPY . /usr/src/app

COPY . /

RUN apt-get update && \
    apt-get install -y wget vim git net-tools

#ENV DOCKERIZE_VERSION v0.2.0
#RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz


ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE=users
ENV TZ=Asia/Seoul

RUN ["ln", "-sf", "/usr/share/zoneinfo/Asia/Seoul", "/etc/localtime"]
RUN ["chmod", "777", "/docker-entrypoint-initdb.d/user.sql"]

EXPOSE 3306
