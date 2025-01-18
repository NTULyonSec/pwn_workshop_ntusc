#!/bin/bash
docker stop d1_challenge
docker container rm -f d1_challenge
docker rmi -f d1_challenge
docker build -t d1_challenge .
docker run -p 8881:8881 -it -d --name d1_challenge d1_challenge
