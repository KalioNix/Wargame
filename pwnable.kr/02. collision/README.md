# 02. collision

## Source Code
```
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
	int* ip = (int*)p;
	int i;
	int res=0;
	for(i=0; i<5; i++){
		res += ip[i];
	}
	return res;
}

int main(int argc, char* argv[]){
	if(argc<2){
		printf("usage : %s [passcode]\n", argv[0]);
		return 0;
	}
	if(strlen(argv[1]) != 20){
		printf("passcode length should be 20 bytes\n");
		return 0;
	}

	if(hashcode == check_password( argv[1] )){
		system("/bin/cat flag");
		return 0;
	}
	else
		printf("wrong passcode.\n");
	return 0;
}
```

* 인자 값의 길이는 20바이트여야 한다.   
```
if(strlen(argv[1]) != 20){
	printf("passcode length should be 20 bytes\n");
	return 0;
}
```   
<br/>

* argv[1]을 인자로 한 check_password함수의 반환값이 hashcode 값과 같다면 flag를 얻을 수 있다.   
```
if(hashcode == check_password( argv[1] )){
	system("/bin/cat flag");
	return 0;
}
```   
<br/>

* check_password 함수는 인자값을 4바이트씩 5개로 잘라서 합친 값을 반환해준다.   
<br/>   


## Writeup

