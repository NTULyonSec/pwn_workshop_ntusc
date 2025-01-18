#!/bin/bash
docker stop d1_challenge
docker container rm -f d1_challenge
docker rmi -f d1_challenge
