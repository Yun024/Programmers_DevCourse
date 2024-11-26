# break : 반복문 정지
# continue : 다음차례로 스킵
basket = ['apple', 'banana', 'orange', 'melon']

for item in basket:
    if item == 'orange':
        continue # 현재 반복 차레 Skip, 아래 코드 무시 
    print(f'{item}을 먹었습니다.')

# 1 2 4 5 7 8..
for n in range(1, 31):
    if n % 3 == 0:
        continue # skip
    print(n)

## while
n = 0
end =  31
while n < end:
    n +=1 
    if n % 3 == 0:
        continue
    print(n)
    
