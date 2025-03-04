# 삼각형 넓이
def calc_triangle(width, height):
    return width * height / 2

# 함수 실행
t1 = calc_triangle(10, 20)
print(t1)

# 변수에 함수 저장
new_func = calc_triangle
t1 = new_func(10, 20)
print(t1)

# 익명함수lambda
# lambda 매개변수 : 식(반환)
lambda_func = lambda width, height : width * height /2
t1 = lambda_func(10, 20)
print(t1)

# 타입 확인
print(type(calc_triangle), calc_triangle)
print(type(new_func), new_func)
print(type(lambda_func), lambda_func) # 주소가 다름 