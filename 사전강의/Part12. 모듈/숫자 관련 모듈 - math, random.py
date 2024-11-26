nums = [1, 99, 2, 3, 4]
print(sum(nums))
print(max(nums),min(nums))

print(abs(-3.14),abs(3.14))
print(divmod(5,3)) # 몫과 나머지
q, m = divmod(5, 3)
print(q,m)

# math
import math
print(math.factorial(2))
print(math.factorial(3))
print(math.factorial(4))
print(math.factorial(5))

## 루트
print(math.sqrt(2))
print(math.sqrt(3))
print(math.sqrt(4))

## 로그함수
print(math.log10(10**2))
print(math.log2(2))
print(math.log(math.e**3))
print(math.log(2,7))

## 삼각함수
print(math.pi)
print(math.sin(math.radians(30)))
print(math.sin(math.radians(45)))
print(math.sin(math.radians(60)))

## 반올림 ceil, floor, trunc
print(math.ceil(3.14 * 10) / 10)
print(math.ceil(-3.14))
print(math.floor(3.14))
print(math.floor(-3.14))
print(math.trunc(3.14))
print(math.trunc(-3.14))

# random
import random
n1 = random.random() # 0~1 float # 시드 지정하지 않음, 고정x
n2 = random.randint(0, 255) # 0~255 int
for _ in range(1000):
    n2 = random.randint(0, 255)
    if n2 ==255:
        print(True)

n3 = random.uniform(0, 255) # 0~255 float
print(n1, n2, n3)

# seed -> 마인크래프트 맵 seed
## 사실 랜덤 구현 불가 -> 난수 알고리즘 -> 임의 값 출력
## 입력 X -> 출력 Y 
## seed는 현재시간을 기준으로 랜덤이 만들어지는 특정 상황을 고정 
random.seed(0)
print(random.random()) # 고정 
print(random.random()) # 위 아래와 값은 다르지만, 이전 실행 결과와 강틈
random.seed() # 고정해제
print(random.random())
print(random.random())

## choice
nums = list(range(1, 46))
print(random.choice(nums))
print(random.sample(nums, 6))

## shuffle
print(nums)
random.shuffle(nums) # 순서 섞임
print(nums) 

# 코딩테스트에 유용한 모듈
## statistics
import statistics
nums = [1, 2, 3, 4, 5, 6, 7, 7, 9, 99]

print(sum(nums)/ len(nums))
print(statistics.mean(nums))
print(statistics.median(nums)) # 중앙값, 짝수일경우 가운데 (두 수 합/2)
print(statistics.mode(nums)) # 최빈값

## heapq
import heapq
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(max(nums), min(nums))

print(max(nums), min(nums))
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print(heapq.nlargest(3, nums)[-1])
print(heapq.nsmallest(3, nums)[-1])
