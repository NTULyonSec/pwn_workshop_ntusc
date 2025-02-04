#!/bin/bash
docker stop session1_challenge
docker container rm -f session1_challenge
docker rmi -f session1_challenge
