# NTU Cybersecurity Club Pwn workshop preinstallation guide

Made by masamuneprog Technical Director

This guide will teach you to install pwntools, pwndbg and docker-ce

It assumes 2 things

1. You already have a updated kali vm
2. Gcc and gdb is installed on your system

Reference images where taken on virtualbox, tested on a fresh install of kali

Commands are in bold

Part 0: Update kali

Run

1. **sudo apt-get update**
2. **sudo apt-get upgrade**

If you have not run this for a long time expect to wait. Alternatively you can get the latest Kali version and reinstall your VM

Part 1: Installation of pwntools

1. **sudo pip3 install pwntools --break-system-packages**
2. Enter the python interpreter by typing **python** and entering **import pwn**
3. If there is no error you are good to go

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc1DrewYaWI2BaEh8hFST7v-mPTBeKpXLsF1UzFxzyIfoSF3tJQkHpYNSNMePfTSiwuBQoforZOGXXR6zSj0AnTz2FtYWzAsAjhLgkZDJ-Hsyoa2BMyKfH6vNZqD74rVW2x9z4vxg?key=_zr6Y7bm0xhbBWpGJRki75P8)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfoJXm2RdT4eZ4XL3ue3MN-RJy3mhRjE843lFuY5bSDHWL_-Gf9ucCVhaVDPCuDr1Jz9w2DeoVJrRp_DYBCIeyQiU19gtk_euv2gRinAZ1L73DYXNvBuLjNw_6eSXNXUPxMkHc4cA?key=_zr6Y7bm0xhbBWpGJRki75P8)

If this does not work, I recommend using a virtual env and installing pwntools in that virtual env. I recommend uv(blazing fast) but you are free to use any  eg Poetry, venv etc

Part 2: Installation of pwndbg

1. Install python 3.13 using **sudo apt install python3.13**
2. Install python 3.13-venv using **sudo apt install python3.13-venv**
3. **git clone [https://github.com/pwndbg/pwndbg](https://github.com/pwndbg/pwndbg)**
4. **cd pwndbg**
5. **./setup.sh**
6. On the terminal enter **gdb-pwndbg**, you should see the pwndbg interface show up

Pwndbg latest requires python3.13 as a dependency, without it new installations fail to create venv with poetry causing failure

Alternatively [https://github.com/apogiatzis/gdb-peda-pwndbg-gef](https://github.com/apogiatzis/gdb-peda-pwndbg-gef) allows you to install the peda,pwndbg and gef together which you might be interested in

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdLWFqRZ5A4BfITx9_Ct8bWpiK54w9D1HngVykF1M0dCy-vamsU1YrQJgNOSIcj6zIWAqu5aCmP57l6Wj6ng8oQ4Gi15H7eXeUz5asAcgbPhgsk9_3kWSffIgxy9wqvzm1zCqWVBg?key=_zr6Y7bm0xhbBWpGJRki75P8](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdLWFqRZ5A4BfITx9_Ct8bWpiK54w9D1HngVykF1M0dCy-vamsU1YrQJgNOSIcj6zIWAqu5aCmP57l6Wj6ng8oQ4Gi15H7eXeUz5asAcgbPhgsk9_3kWSffIgxy9wqvzm1zCqWVBg?key=_zr6Y7bm0xhbBWpGJRki75P8)

                         If the systems prompts you for any installation and updates type in yes

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXeHHo9Krwjjz6DvKqnWPiXE2X-YhtVG07v9ttvBRF8ybwV_jbMxxRKDs1cqppr_J9PlVaYomdyjmz5OMAeKAJiHElXRdaHjYygxqyO_7R1Oj5l4g9qKcOfjAFiitdN-eDkIzi0oyA?key=_zr6Y7bm0xhbBWpGJRki75P8](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeHHo9Krwjjz6DvKqnWPiXE2X-YhtVG07v9ttvBRF8ybwV_jbMxxRKDs1cqppr_J9PlVaYomdyjmz5OMAeKAJiHElXRdaHjYygxqyO_7R1Oj5l4g9qKcOfjAFiitdN-eDkIzi0oyA?key=_zr6Y7bm0xhbBWpGJRki75P8)

                                                                              pwndbg interface

Docker Ce([Source](https://www.kali.org/docs/containers/installing-docker-on-kali/))

1. **printf "%s\n" "deb [arch=amd64] https://download.docker.com/linux/debian bookworm stable" |\sudo tee /etc/apt/sources.list.d/docker-ce.list**
2. **curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -**
3. **sudo apt-key fingerprint 0EBFCD88**
4. If 2 and 3 fails with apt-key not avail try this **curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker.gpg**
5. **sudo apt update(Ignore error)**
6. **sudo apt install -y docker-ce docker-ce-cli containerd.io**
7. If the package is not found, run **sudo su,**
8. Run **echo "deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list**
9. Rerun steps 5 and 6
10. To check if the package is installed properly enter

**sudo docker run hello-world**

Upon successful installation

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXehLc5vmKVsC1DYzkSqNWb26OHS0OTqMgHR8o2edGg_VP46L_z7Uqc7XKArGUJz0f95IMtIt2UfYFFOsRu1GORNR7U43SfZk6-_ctSe5m7sc2kagVK5YWkxHduy7spgh3HU01rc?key=_zr6Y7bm0xhbBWpGJRki75P8](https://lh7-rt.googleusercontent.com/docsz/AD_4nXehLc5vmKVsC1DYzkSqNWb26OHS0OTqMgHR8o2edGg_VP46L_z7Uqc7XKArGUJz0f95IMtIt2UfYFFOsRu1GORNR7U43SfZk6-_ctSe5m7sc2kagVK5YWkxHduy7spgh3HU01rc?key=_zr6Y7bm0xhbBWpGJRki75P8)

[https://lh7-rt.googleusercontent.com/docsz/AD_4nXdf4d1ojGv7krsKW7j_TvBnJZaxz_i27pcyGnHksEP3a-E0lDvrjbAkfY829hcrFJFg5rEkcnBrmOF-Y5H93jusISINOiMEhBC0R_QRi1YUKQjOMKVsh7E5zDKcK_IvIjmeoyoI?key=_zr6Y7bm0xhbBWpGJRki75P8](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdf4d1ojGv7krsKW7j_TvBnJZaxz_i27pcyGnHksEP3a-E0lDvrjbAkfY829hcrFJFg5rEkcnBrmOF-Y5H93jusISINOiMEhBC0R_QRi1YUKQjOMKVsh7E5zDKcK_IvIjmeoyoI?key=_zr6Y7bm0xhbBWpGJRki75P8)

                                                                            Ignore if you see this

NAT Setup

For NAT, just google for how to configure NAT for whatever VM software you are using.
