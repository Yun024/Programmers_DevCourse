# 프로그래밍 테스트에서 여러 입력 값 받기 
## a,b = map(int,input().split())

# split
text = "asdf asdf asdf asdf asdf asdf asdf"
data = text.split() 
print(data)
## 인자에 아무것도 넣지 않을 경우 공백을 기준으로 분리
data1 = text.split('f ')
print(data1)

## map : list comprehension보다 가독성이 좋음 
user_input = list(map(int,input().split()))
print(user_input)

## list comprehension : 함수가 들어가면 가독성이 나빠짐
user_input = [int(n) for n in input().split()]
print(user_input)