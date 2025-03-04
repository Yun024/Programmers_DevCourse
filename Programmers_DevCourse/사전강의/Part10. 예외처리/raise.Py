# raise
# raise KeyboardInterrupt
# raise ZeroDivisionError

# 값을 음수로 받을 경우 ValueError
number = int(input("Test Number : "))
if number < 0:
    raise ValueError("Negative numbers are not allowed")

## raise 코드는 에러메세지 출력 후 모든 프로그램 종료 
## try-except의 경우 프로그램이 종료되지 않음
## Traceback 안나옴, ValueError이라는 메세지도 안나옴
## >>> 즉 아래에 코드가 더 있을 경우 에러 메세지 출력 후 실행

# 오류 생성 +  제어
try:
    number = int(input("Test Number : "))
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
except ValueError as ve:
    print(ve)

## 삼각형의 넓이 
def calc_triangle(width, height):
    if width < 0 or height < 0 :
        raise ValueError("Negative numbers are not allowed")
    area = width * height / 2
    return area

## 함수 실행
t1 = calc_triangle(10, 20)
t2 = calc_triangle(100, 200)
print(t1+t2)
t3 = calc_triangle(-100, 200)
