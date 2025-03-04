# tuple 튜플
# create
eyes = (1.9,2.0)
users = ('Allen','Chen','John','May')

# access
print(eyes[0])
print(users[2])

# update -> 리스트는 가능, 튜플 불가능
## eyes[0] = 0.1
## users[2] ='Spencer'

# del -> 리스트o, 튜플x
## del eyes[0]
## del users[2]

## 생성 이후 수정 불가능 -> 튜플
## 생성 이후 수정 가능 -> 리스트

RED = (255, 0, 0) # 고정형 데이터 : 상수
customr_color = [255, 0, 0] # 변수