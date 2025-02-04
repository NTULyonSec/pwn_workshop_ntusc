#!/bin/bash

gcc $1.c -o $1 -z execstack -fno-stack-protector -no-pie
