#!/usr/bin/python3

# import pwntools library
from pwn import *

# ---- loading binary to pwntools ----

# (1) simple loading of binary
# Example:
elf = context.binary = ELF("./bof2rop")

p = process(elf.path)

# (2) simple loading of binary (with pwndbg launched)
# Example:
#p = gdb.debug(elf.path,'''
#break main
#continue
#''')

# (3) List out all available ROP gadgets. can be done in two ways
## a. Run following command in terminal to get the full list of gadgets: ROPGadget --binary bof2rop > ropgadgets.txt
## b. Use pwntools to retrieve the ROP gadgets from the ELF object (using the ROP library)

## For beginners, we're gonna go with method (a) first to familiarise the concept.

# (4) Figure out what is the end goal (what syscall function you want to do)

## Link: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md

## Based on the link above, we want to use the execve() function call that allows us to get a shell via /bin/sh.
## Requirements are as follows:
### RAX = 0x3b (this is the function reference number, or NR)
#### to do this, we need a ROP gadget that does 'pop rax', followed by the value of RAX to set.

### RDI = 1st argument for execve(), in this case it is a POINTER to the string "/bin/sh"
#### as there's no reference for /bin/sh, what we can do is to store the string in a memory region whereby write permissions are allowed (load up GDB on the binary, set a breakpoint and run, and then type 'vmmap')
#### in this example we have a memory region between 0x404000 and 0x405000 that we can put the string in (due to the rw-p permissions), so let's use 0x404000 as the string addr
#### Plan here is to:
##### - Put the /bin/sh string into RCX
##### - Put the string address to store /bin/sh to RDI
##### - Use a MOV instruction to move contents of RCX to the relative memory location of RDI value

### RSI = 2nd argument for execve(), but we do not need that. so can set to 0

### RDX = 3rd argument for execve(), but we do not need that. so can set to 0

## Once all these registers are set with the correct values, run the 'syscall' instruction.

# ---- constructing the payload ---
## still need to figure out what is the offset first.
offset_num = 0
payload = b'A' * offset_num 

p.sendline(payload)
p.interactive()
