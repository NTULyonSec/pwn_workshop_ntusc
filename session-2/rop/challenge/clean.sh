#!/bin/bash
docker stop rop_challenge
docker container rm -f rop_challenge
docker rmi -f rop_challenge
