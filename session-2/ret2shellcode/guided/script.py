#!/usr/bin/python3

# import pwntools library
from pwn import *

# ---- loading the binary as an ELF (to reference file characteristics)

#elf = ELF("/path/to/binary")

# leave this setting here (this forces pwntools to operate within a Linux x86-64 environment when loading the binary)

context.update(arch='x86_64',os='linux')
# ---- loading binary to pwntools ----

# (1) simple loading of binary
# Example:
# p = process(elf.path)

# (2) simple loading of binary (with pwndbg launched)
# Example:
# p = gdb.debug(elf.path,'''
# break main
# continue
#''')

# ---- constructing the payload ---
# in addition to the usual workflow, you will also need these syntaxes:

## This variable below finds an address within the binary that points to the JMP RSP instruction.
# JMP_RSP_ADDR = p64(next(elf.search(asm("jmp rsp"))))

## This variable generates the necessary shellcode (set of assembly instructions) to give you a shell
# shellcode = asm(shellcraft.amd64.sh())

# usual workflow:
# (1) let's flood the input with lots of 'A's
# pl_sz = <put your number here>
# payload = b'A'* pl_sz
#
# (2) send it to the program
# p.sendline(payload)
#
# (3) get an interactive interface (this is for later to get a shell, but we'll leave this last line for now)
# p.interactive()

