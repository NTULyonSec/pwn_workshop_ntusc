#!/bin/bash
docker stop session1_challenge
docker container rm -f session1_challenge
docker rmi -f session1_challenge
docker build -t session1_challenge .
docker run -p 8881:8881 -it -d --name session1_challenge session1_challenge
