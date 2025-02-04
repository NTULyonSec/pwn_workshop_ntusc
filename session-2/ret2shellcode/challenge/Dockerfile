FROM ubuntu:24.04
RUN apt-get update
RUN apt-get install -y ucspi-tcp-ipv6 gcc gcc-multilib g++-multilib

RUN useradd -u 8888 -m pwn
RUN mkdir -p /home/pwn
RUN chown -R pwn:pwn /home/pwn

ADD challenge.c /home/pwn/challenge.c
RUN gcc -o /home/pwn/pwnie /home/pwn/challenge.c -fno-stack-protector -z execstack -no-pie

RUN chmod +x /home/pwn/pwnie
WORKDIR /home/pwn

CMD ["tcpserver","-t","50","-u","8888","-g","8888","-RHl0","0.0.0.0","8882","/home/pwn/pwnie"]
