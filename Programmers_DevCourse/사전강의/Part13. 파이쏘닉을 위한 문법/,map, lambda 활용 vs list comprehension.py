# map(적용함수, 시퀀스데이터)
# 각 요소를 적용함수로 넣었을 떄의 return값으로 남겨 반환
# 모든 요소에 대해 처리한다는 것이 list comprehension과 유사해보임

chars = ['1', '2', '3', '4']
nums = list(map(int,chars)) # 비파괴적
print(nums, chars)

def positive_number(number):
    return number > 0

nums = [-3, 3, 5, -5, 1, 0, 1, 3, 8, -8]
new_nums = list(map(positive_number, nums))
print(new_nums)

# map, lambda 
## positive_number 함수를 굳이 만들어야 될까? 일회성으로 사용하고 싶음
nums = [-3, 3, 5, -5, 1, 0, 1, 3, 8, -8]
new_nums = list(map(lambda x : x > 0, nums))
print(new_nums)


# 리스트 컴프리헨션과 map의 비교
## 빌트인 함수 - list comprehension
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
chars = [str(n) for n in nums]
print(chars)

## 빌트인 함수 - map 
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
chars = list(map(str, nums))
print(chars)

## 기본 연산 - list comprehension
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [n**2 for n in nums]
print(new_nums)

## 기본연산 - map -> 무조건 함수 지정
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(map(lambda x: x**2, nums))
print(new_nums)

## lambda를 이용한 연산 + list comprehension
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = [(lambda x:2*x+1)(n) for n in nums]
new_nums = [2*n+1 for n in nums]
print(new_nums)

## lambda를 이용한 연산 + map
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = list(map(lambda x: 2*x+1, nums))
print(new_nums)

## 굳이 list comprehension에 람다를 사용할 필요 없음 
## "가능"하다면 map이 아닌 list comprehension 사용 