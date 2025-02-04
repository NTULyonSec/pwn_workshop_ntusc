# Session 1 Challenge
The Session 1 challenge simulates a typical pwn deployment that is done over the network (represented as a network service). Participants would usually need to connect to the network and exploit it accordingly 
## Pre-Requisites
Ensure that you have docker installed. To check, run the following command:
```
docker ps
```
If it is installed correctly, you should get some form of output that looks like this:
```
└─# docker ps               
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

```
## Challenge Setup
There's already a start script that I have made that will do the following:
- Remove any instances of the session1_challenge docker image
- Build the docker image based on the Dockerfile
- Launch a docker container based on the newly-built docker image.

For you, all you need to do is just to clone this repository and run the script:
```
cd pwn_workshop_ntusc/session1/challenge; chmod +x setup.sh; ./setup.sh
```

If all goes well, run the 'docker ps' command and you should see something like this:

```
└─# docker ps 
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                       NAMES
ddf90ddb699c   session1_challenge   "tcpserver -t 50 -u …"   5 minutes ago   Up 5 minutes   0.0.0.0:8881->8881/tcp, :::8881->8881/tcp   session1_challenge

```

To test if it works, use netcat to connect to port 8881 on localhost, like this:
```
nc localhost 8881
```
## Tips for the challenge
- It is not possible for you to just start doing the analysis by compiling the challenge.c code and analysing it from the compiled binary (mainly because it is in a different Linux distro, look at the first line of the Dockerfile).
<br><br>
- As such you need to extract the compiled binary from the Dockerfile. Enter this command to continue:
```
docker cp session1_challenge:/home/pwn/pwnie .
```
The 'pwnie' binary will be copied into your Kali machine.
- Create the exploit code first locally within your machine to make sure it works. Once it works fine, you simply need to change the code to connect to the remote network service:
```
p = remote("localhost",8881)
``` 
