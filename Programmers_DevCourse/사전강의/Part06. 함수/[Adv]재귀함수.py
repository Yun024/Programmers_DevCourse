# n, n-1, n-2, ... 1 또는 0까지 
# 재귀함수(Recursion)

def countdown(number):
    print(number)
    if number == 0:
        return 
    else:
        return countdown(number-1)

countdown(10)

## 재귀 정지조건이 없으면 에러 발생 

# 팩토리얼
## 4! =  3 * 3!
## 3! =  3 * 2!
## 2! =  2 * 1

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)
    
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

## 디버그모드의 호출스택을 통해 파트의 진행상황을 파악할 수 있음