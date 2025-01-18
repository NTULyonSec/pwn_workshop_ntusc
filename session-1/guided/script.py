#!/usr/bin/python3

# import pwntools library
from pwn import *

# ---- loading binary to pwntools ----

# (1) simple loading of binary
# Example:
# p = process("/path/to/binary")

# (2) simple loading of binary (with pwndbg launched)
# Example:
# p = gdb.debug("/path/to/binary",'''
# break main
# continue
#''')

# ---- constructing the payload ---

# (1) let's flood the input with lots of 'A's
# pl_sz = <put your number here>
# payload = b'A'* pl_sz
#
# (2) send it to the program
# p.sendline(payload)
#
# (3) get an interactive interface (this is for later to get a shell, but we'll leave this last line for now)
# p.interactive()
