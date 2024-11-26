# while 조건 > while True if break
## while 조건식
goal_num = 10000000
step = 2
result = 1

count = 0
while result < goal_num:
    result *= step
    count += 1
print(f'count:{count} result:{result}')

## while True:
goal_num = 10000000
step = 2
result = 1
count = 0 
while True:
    result *= step
    count +=1
    if result >= goal_num:
        break
    if result < 0:
        print('음수면 종료')
        break
print(f'count:{count} result:{result}')


## while 조건식
import random, time

learning_score = random.randint(1, 100)
while learning_score < 90:
    print(f'학습 스코어 미달 : {learning_score}')
    learning_score = random.randint(1, 100)
    time.sleep(.5)
print(f'최종 학습 스코어 : {learning_score}')

## while True : 원하는 값을 얻었음에도 한번 while을 수행 > 개선
learning_score = random.randint(1, 100)

while True:
    if learning_score > 90:
        break
    print(f'학습 스코어 미달 : {learning_score}')
    learning_score = random.randint(1, 100)
    time.sleep(.5)
print(f'최종 학습 스코어 : {learning_score}')