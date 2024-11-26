try: 
    1/0 # zeroDivisionError
except:
    pass # 아무것도 하지 않음 


try: 
    1/0
except Exception as e:
    print(e)
print("정상 종료")

try:
    1 + "가" # TypeError
    int('가') # ValueError
except ValueError as ve:
    print(f'>>> {ve}')
except Exception as e:
    print(f'>>> {e}')

### 첫번째 오류만 실행하여 오류 발생 
### 두번째 오류도 실행하려면 2개의 try문 혹은 반복문에 오류를 넣고 실행
### excpet Exception으로 작성해야 Keyboard Error를 통해 정지 가능
### 더 안전하게 tyr, except문 사용 가능 (컨틀롤 C)

try:
    num = 3/0
    print(num)
except Exception as e:
    print(e)
finally:
    print('try문 종료 - 마무리 수행')

## 최종정리
try:
    # 수행, 시도할 코드
    pass
except ValueError:
    # ValueError 예외처리
    pass
except (ZeroDivisionError, TypeError):
    # ZeroDivisionError, TypeError 다중 예외 처리
    pass
except: # Exception 
    # 그외 예외 + default 예외 처리
    pass
finally:
    # 무조건적으로 마무리코드로 수행은 되야한다!
    pass

# 처리할 데이터에 예상치 못한 값, 상황이 발생할 때
# y = 2/x +1
nums = [0, 3, 9, 12, 'a', 'x', 15]

for x in nums:
    try:
        print(f'2/{x} +1 = {2/x +1}')
    except (ZeroDivisionError, TypeError) as e:
        print(f'>>> Error : {e}')

## 내가 예상치 못한 상황이 발생했을 떄 프로그램 종료할거면 아래 코드 스킵
    except Exception as e: 
        print(e)