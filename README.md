# Pwn 101 Workshop for NTU Cybersecurity Club
Designed by: Sayed Hamzah (@BaeSenseii), NTU Alumni
## Overview
This is a simple pwn 101 workshop that was designed to introduce participants into the basics. Currently this workshop is split into a two-part series (refer to the subsequent subheaders below), and this repository only serves as a code base for the exercises designed during these workshops.
### Session 1
- Quick Recap of Assembly Instructions, Registers and Stack
- pwndbg and pwntools, a pwn junkie's best friend
-- launching the binary via pwntools
-- sending input via pwntools
-- launching pwndbg while launching the binary from start
- Buffer Overflow
-- Causing the crash
-- Finding the offset that allows us to control the value of the RIP register.
-- What to do after Buffer Overflow? easiest: ret2win
### Session 2
- Other Buffer Overflow outcomes (ret2shellcode)
- x64 Syscalls
- Binary Protection Mechanisms & Return Oriented Programming (ROP)
