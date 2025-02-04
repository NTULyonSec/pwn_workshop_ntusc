#!/bin/bash
docker stop rop_challenge
docker container rm -f rop_challenge
docker rmi -f rop_challenge
docker build -t rop_challenge .
docker run -p 8883:8883 -it -d --name rop_challenge rop_challenge
