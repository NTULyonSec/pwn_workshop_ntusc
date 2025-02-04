#!/bin/bash
docker stop ret2shellcode_challenge
docker container rm -f ret2shellcode_challenge
docker rmi -f ret2shellcode_challenge
