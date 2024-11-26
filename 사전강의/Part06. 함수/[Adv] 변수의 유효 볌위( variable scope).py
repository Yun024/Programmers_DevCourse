# Global scope , Local scope
## 디버그 모드 실행
def add(a,b):
    ## globla c 로컬영역에서 글로벌 변수를 변경하는 것은 추천x
    ## 코드에 혼잡성 발생 
    print(a, c) # a는 로컬, c는 전역 
    return a + b

a = 1
b = 2
c = 3
add(4,5)