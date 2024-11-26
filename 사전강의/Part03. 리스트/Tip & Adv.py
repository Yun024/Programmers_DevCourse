# 데이터 구조 이해를 돕는 도구 - Python Tutor
a = 3
b = 'test'
school = [
    ['Allen','Chen','John','May'],
    ['Bllen','Bhen','Bohn','Bay'],
    ['Cllen','Chen','Cohn','Cay']
]

school[0][1] = 'Spencer'
school[2][0] = 'Spencer'

# 개발자의 숫자가 0부터인 이유
[1,2,3,4,5,6,7,8,9,10,11,12] ## 1 <= i < 13
[0,1,2,3,4,5,6,7,8,9,10,11]  ## 0 <= i < 12
## 이때 1인 자기자신을 0으로 표현하면 이동했을 떄를 계산하기 수월함
## 1에서 우측2번 이동하면 3번집이 나옴 
## 0에서 우측2번 이동하면 2번집이 나옴 <<<< 

# list 참조와 복사
score_A = [80,70,60,50,40]
score_B = score_A # [80,70,60,50,40]
score_B[0] = 100 # [100,70,60,50,40]
print(score_A)
print(score_B)

score_A = [80,70,60,50,40]
score_B = score_A.copy() # [80,70,60,50,40]
score_B[0] = 100
print(score_A)

score_B = score_A[:]
score_B[0] = 100
print(score_A)

# id (메모리 확인 함수)
score_B = score_A
print(id(score_A))
print(id(score_B))

score_B = score_A[:]
print(id(score_A))
print(id(score_B))

# is (같은 메모리인지 확인하는 함수)
score_B = score_A
print(score_A is score_B)
score_B = score_A[:]
print(score_A is score_B)