# int_convert_str.py
## 3 vs "3" : int vs str
year = 2020
month = 12
day = 25
birth = year + month + day
print(birth) # 생년월일이 아닌 숫자로 인식

year = str(2020) # '2020'
month = str(12)  # '12'
day = str(25)    # '25'
birth = year + month + day
print(birth)


# str_convert_int.py
year = '2020'
current_year = '2200'
##  print(current_year - year)

year = int('2020')
current_year = int('2200')
print(current_year - year)

# str(v) string
# int(v) integer
num1 = int(3.0)
print(num1)
num2 = float(3)
print(num2)
## num3 = int("가나다") # valueError
## num4 = int('3.0')   # valueError : -3,3일때만 변환가능


