# floating_point_number expression
num1 = 123.456789

## round()
num2 = round(num1,-1) # round(,0), round()의 차이는 float와 int
print(num2)

## format() -> 문자열
num2 = "{0:.2f}".format(num1)
print(num2) # str -> int float 형변환 필요

## fstring -> 문자열
num2 = f"{num1:.2f}"
print(num2)