import time 
## time.py, 동일한 파일명으로 만들어 놓으면 에러 발생할 수 있음
## time은 시간, datetime는 시각

# time.sleep(int|float)
time.sleep(1)
## 프로그램의 흐름을 잠시 중지시킴 
print('start')
## time.sleep(1)
print('end')

# time.time()
start = time.time() 
## 유닉스시간 UTC 1970.1.1 00:00:00 ~ 몇 초가 지났는지
print(start)

## 시간 측정
print('------')
total = 0
for i in range(100000):
    total += i 
    #print(total)
print(total)
end = time.time()
print(end - start) # 실행 시작 전과 끝난 후를 뺄셈
print('--------')

# datetime
import datetime
now = datetime.datetime.now() # 모듈, 클래스, 메서드 순서
print(now)

from datetime import datetime as dt, timedelta as td, timezone as tz ## *는 all
now = dt.now()
print(now, type(now))

# 시각 - 시각 = 시간차이(timedelta)
print('--------')
future = dt(2200, 11, 18) # 없는게 아니라 0으로 초기화
print(future.hour, future)
interval = future - now
print(interval, type(interval)) # 시간을 뺄셈하니 클래스 td출력

# 시간차이
period = td(days=1000, hours=10)
print(period)
print(now - period)

# 시간 원하는 포멧(문자열)
print('--------')
print(f'{now.hour}:{now.minute}')
date1 = now.strftime("%Y %m %d %p %I %H %M %S %a")
date2 = now.strftime("%Y-%m-%d-%p %I %M %S %a")
date3 = now.strftime("%Y년 %m월 %d일 %p %I %M %S %a")

print(date1)
print(date2)
print(date3)

# 국가 시간 미국 LA - 7
print('--------')
nz_tz1 = tz(td(hours=-7))
nz_tz2 = tz(td(hours=+9))
nz_now1 = dt.now(tz=nz_tz1)
nz_now2 = dt.now(tz=nz_tz2)
print(nz_now1)
print(nz_now2)

