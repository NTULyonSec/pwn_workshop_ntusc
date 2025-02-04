#!/bin/bash
docker stop ret2shellcode_challenge
docker container rm -f ret2shellcode_challenge
docker rmi -f ret2shellcode_challenge
docker build -t ret2shellcode_challenge .
docker run -p 8882:8882 -it -d --name ret2shellcode_challenge ret2shellcode_challenge
