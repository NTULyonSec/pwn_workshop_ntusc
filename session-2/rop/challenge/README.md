# Session 2 (Return Oriented Programming) Challenge
The Session 2 ROP challenge simulates a typical pwn deployment that is done over the network (represented as a network service). Participants would usually need to connect to the network and exploit it accordingly 
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
- Remove any instances of the d1_challenge docker image
- Build the docker image based on the Dockerfile
- Launch a docker container based on the newly-built docker image.

For you, all you need to do is just to clone this repository and run the script:
```
cd pwn_workshop_ntusc/session2/rop/challenge; chmod +x setup.sh; ./setup.sh
```

If all goes well, run the 'docker ps' command and you should see something like this:

```
└─# docker ps 
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                                       NAMES
d8b6ebc0ede9   rop_challenge   "tcpserver -t 50 -u …"   9 minutes ago   Up 9 minutes   0.0.0.0:8883->8883/tcp, :::8883->8883/tcp   rop_challenge
```

To test if it works, use netcat to connect to port 8881 on localhost, like this:
```
nc localhost 8883
```
## Tips for the challenge
- It is not possible for you to just start doing the analysis by compiling the challenge.c code and analysing it from the compiled binary (mainly because it is in a different Linux distro, look at the first line of the Dockerfile).
<br><br>
- As such you need to extract the compiled binary from the Dockerfile. Enter this command to continue:
```
docker cp rop_challenge:/home/pwn/pwnie .
```
The 'pwnie' binary will be copied into your Kali machine.
- Create the exploit code first locally within your machine to make sure it works. Once it works fine, you simply need to change the code to connect to the remote network service:
```
p = remote("localhost",8883)
```

- This time round this program does not have any source code as it was already found pre-compiled (btw this challenge was not built by me, it was from one of the CTFs that i did).
