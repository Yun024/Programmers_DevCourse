# while vs for
# for : user는 원본 데이터 아님 
users = ['Allen', 'Chen', 'John', 'May']
for user in users:
    print(f'{user}가 입장을 했습니다.')

# while : users[index]는 원본데이터 
users = ['Allen', 'Chen', 'John', 'May']
index = 0
while index < len(users):
    print(f'{users[index]}가 퇴장하셨습니다.')
    index +=1

## while문 : 무한 반복 가능
goal_num = 10000000
step = 2
result = 1

count = 0
while result < goal_num:
    result *= step
    count += 1
print(f'count:{count} result:{result}')

## for문 : 정해진 횟수, 데이터 개수처럼 한계치가 정해진 상황
## Limit가 주어진 상황으로 반복 
goal_num = 10000000
step = 2
result = 1

for count in range(1,100):
    result *= 2
    count +=1
    if result >= goal_num:
        print(f'count:{count} result:{result}')
        break
