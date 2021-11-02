#!/bin/sh

if [ $# -eq 0 ];then
    docker-compose build
    #docker stop  $(sudo docker  ps -a -q)
    #docker rm   $(sudo docker  ps -a -q)
    docker-compose up -d
else
      # docker stop  $(docker ps --filter name=$1 -aq)
      # docker rm   $(docker ps --filter name=$1 -aq)
      docker-compose up -d --no-deps --build $1
fi
