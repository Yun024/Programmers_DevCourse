# filter(기줂마수, 시퀀스데이터)
# for로 양수만 추출
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = []
for n in nums:
    if n > 0:
        new_nums.append(n)
print(new_nums)

# 함수
def positive_number_list(nums):    
    new_nums = []
    for n in nums:
        if n > 0:
            new_nums.append(n)
    return(new_nums)

nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
print(positive_number_list(nums))

# filter + map
def positive_number(n):
    return n > 0

nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(filter(positive_number, nums)) # 기준함수
print(new_nums)
new_nums = list(map(positive_number, nums)) # 적용함수
print(new_nums)

## lambda + filter
new_nums = filter(lambda x: x>0, nums) # 기준함수
print(list(new_nums))

# list comprehension + 3항 연산자 if else
## 조건문이 가운데n에서 적용
new_nums = [n for n in nums if n>0 ]
print(new_nums)

## 조건문이 맨 앞n에서 적용
new_nums = [n if n> 0 else False for n in nums ]
print(new_nums)

## 1. 리컴, 2. map, 3.filter 