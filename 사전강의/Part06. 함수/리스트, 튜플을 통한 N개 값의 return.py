"""온도 표기법
섭씨(Celsius) ℃ = (℉ - 32) / 1.8 = K - 273.15
화씨(Fahrenheit) ℉ = (℃ * 1.8) + 32 = (K - 273.15) * 1.8 +32
절대온도(Kelvin) K = ℃ + 273.15, = (℉ - 32) / 1.8 + 273.15
"""

# 온도 표기법
def convert_temperature(c):
    c = c
    f = c * 1.8 + 32
    k = c + 273.15
    return c,f,k 

## 괄호를 제거하고 여러 값을 연속으로 return할 경우 자동으로 튜플 반환

## 함수 실행
t = 25.5
t_expr = convert_temperature(t)
print(t_expr)

# 입력받은 온도에 따라 온도를 계산해주는 함수
def convert_temperature(t, unit):
    if unit == "C":
        c = t
        f = c * 1.8 + 32
        k = c + 273.15
        return c,f,k    
    elif unit =="F":
        f = t
        c = (f - 32) / 1.8
        k = c + 273.15
    elif unit == "K":
        k = t
        c = k - 273.15
        f = c * 1.8 + 32
    else:
        c, f, k = False, False, False
    return c,f,k

## 함수 실행
t = 25.5
t_expr = convert_temperature(t, 'C')
print(t_expr)

t_expr = convert_temperature(t, 'F')
print(t_expr)

t_expr = convert_temperature(t, 'K')
print(t_expr)

t_expr = convert_temperature(t, 'A')
print(t_expr)