# str_func.py
## upper 
text = "AbCdE"
text = text.upper() 

### print(text.upper())
### non-destructive : 비파괴적 : 실행 전과 후의 원본이 바뀌지 않았음 

print(text)

## lower
text = "AbCdE"
text = text.lower()
print(text)

## count
cnt_C = "aCbCdCeC".count("C")
print(cnt_C)

## isalpha = 알파벳 체크 : 띄어쓰기, 숫자도 잡아냄 
text = "10 years old" 
check = text.isalpha()
print(check)

## isnumeric = 숫자만 체크
text = "10 years old"
check = text.isnumeric()
print(check)

## isalnum - 문자 숫자로만 체크
text = "10살입니다"  # "10yearsold"
check = text.isalnum()
print(check)

## ljust, center, rjust
text1 = "hello".ljust(10,)
text2 = "hello".center(10)
text3 = "hello".rjust(10)
print(text1, text2, text3, sep ="-")

## len(v) - 길이 length
text = "abcdefg"
print(len(text))