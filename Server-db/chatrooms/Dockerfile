# Dockerfile for Database

FROM mariadb:10.6.4-focal
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN apt-get update && \
    apt-get install -y wget

ENV DOCKERIZE_VERSION v0.2.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz


ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE=chatrooms
ENV TZ=Asia/Seoul

ENTRYPOINT ["/usr/src/app/docker-compose-initdb.d"]

EXPOSE 3306