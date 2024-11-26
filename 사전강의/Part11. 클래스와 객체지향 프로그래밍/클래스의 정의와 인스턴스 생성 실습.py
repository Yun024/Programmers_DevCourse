# 클래스를 만드는 기본적인 코드
class User: # CapWord ,snake 아님
    pass

## 생산
user1 = User()
user2 = User()
member = [User(),User()]

## User의 출력 방식이 정의되어 있지 않아 메모리 출력
'''
print(user1)
print(member)
'''

# 게임
## 캐릭터 속성(attr)- 이름, 에너지, 레벨
## 캐릭터 함수(method) - 먹는 것, 레벨 업


name = 'spencer'
energy = 50
level = 1

def show():
    print(f'STAT : name:{name}, energey:{energy}, level:{level}')

def eat(food):
    global energy
    if food =='이상한사탕':
        energy += 100
    elif food in ['빵','김밥','라면']:
        energy +=30
    else:
        energy +=10

def level_up():
    global energy, level
    if energy < 100:
        print(f'실패 : 에너지 100 필요 - energy:{energy}')
    else:
        energy -= 100
        level += 1
        print(f'레벨 업 : energy{energy} level: {level}')

## 메인 영역
'''
show()
eat('빵')
show()
eat('이상한사탕')
level_up()
show()
'''



# class 생성
class User():
    # initialize - overide
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.level = 1

    def __str__(self):
        return f'STAT : name:{self.name}, energey:{self.energy}, level:{self.level}'

    def show(self):
        print(f'STAT : name:{self.name}, energey:{self.energy}, level:{self.level}')

    def eat(self, food):
        if food =='이상한사탕':
            self.energy += 100
        elif food in ['빵','김밥','라면']:
            self.energy +=30
        else:
            self.energy +=10

    def level_up(self):
        if self.energy < 100:
            print(f'실패 : 에너지 {100-self.energy} 필요 - energy:{self.energy}')
        else:
            self.energy -= 100
            self.level += 1
            print(f'레벨 업 : energy{self.energy} level: {self.level}')

## 메인 영역
user1 = User('Spencer')
user2 = User('Mussg')
print(user1)
print(user1.name)
print(user1.level)

## 먹는 동작
user1.eat('이상한사탕')
user2.eat('빵')
user1.show()
user2.show()

## 레벨 업
user1.level_up()
user2.level_up()

## print : 문자열로 변환하여 출력 
print(user1, user2) # str주석처리 
### <__main__.User object at 0x000002208783BC70> <__main__.User object at 0x000002208783BFD0> 
### STAT : name:Spencer, energey:50, level:2 STAT : name:Mussg, energey:80, level:1
t = str(user1)
print(t + 'abc')

str #컨트롤 클릭하면 클래스 설계도 보여줌
int 