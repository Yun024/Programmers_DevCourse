# bug name = "python bug"
# number of legs = 0
# 10full = 3

# 시작을 숫자로 하면 안됨
## 7 num = 0
num_7 = 0

# 빈칸이 들어가서는 안됨
## number of legs = 0 
number_of_legs = 0 # snake_case - python
NumberOfLegs = 0 # CapWorld, Camelcase - class
numberOfLegs = 0 # mixedCase - 잘쓰지 않음

# 소문자 대문자
GRAVITY = 9.8  # 지구의 중력은 9.8로 변하지 않는 값 : 대문자
name = "머쓱이" # 변할 수 있는 값 : 소문자
age = 10 

# 한글 : Python utf-8덕분에 에서 사용할 수 있지만 영어 의외의 변수명 추천x
이름 ="스펜서"
나이 = 99
print(이름,나이)

name = "스펜서"
age = 99
print(name,age)

# 특수문자 _ 허용

# 파이썬 예약된 용어 사용x
## if, for, break
import keyword
print(keyword.kwlist)
'''
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

# 자주 사용하는 함수
## print = "text"
print(3)

# 보너스 - 함수 변수에 저장하기
출력 = print
출력("와 이게 되네")