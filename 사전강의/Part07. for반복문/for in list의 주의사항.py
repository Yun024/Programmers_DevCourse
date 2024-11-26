# for문 도중 member의 remove > 넘어가는 데이터가 생김
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']

for user in member:
    if user[0] in ['A', 'a']:
        member.remove(user)
print(member)
## 기대 :['Spencer', 'Chen', 'John', 'Darby']
## 실제 :['Spencer', 'Allen', 'Chen', 'John', 'Andy', 'Darby']



# for문 도중 member의 append > 끝나지않음
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']

## for user in member:
##     if user[0] in ['A', 'a']:
##         member.append(user)
## print(member)
## 기대 :['Spencer', 'Adela', 'Adela', 'Allen', 'Allen', 'Chen', 'John', 'Albert', 'Albert', 'Andy', 'Andy', 'Darby']
## 실제 :for문이 끝나지 않음 계속 A로 시작되는 member 추가


# for문 도중 member의 remove > 개선
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']

for user in member.copy():
    if user[0] in ['A', 'a']:
        member.remove(user)
print(member)
## 기대 :['Spencer', 'Chen', 'John', 'Darby']
## 실제 :['Spencer', 'Chen', 'John', 'Darby']

# for문 도중 member의 append > 개선
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']

for user in member.copy():
    if user[0] in ['A', 'a']:
        member.append(user)
print(member)
## 기대 :['Spencer', 'Adela', 'Adela', 'Allen', 'Allen', 'Chen', 'John', 'Albert', 'Albert', 'Andy', 'Andy', 'Darby']
## 실제 :['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby', 'Adela', 'Allen', 'Albert', 'Andy']

# for문에서의 수정(update) >> user는 카피 값이라 변경x
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for user in member:
    if user[0] in ['A', 'a']:
        user = 0 
print(member)

## 기대 : ['Spencer',0 ,0 , 'Chen', 'John',0 ,0 , 'Darby']
## 실제 : ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']


# for문에서의 수정(update) 개선 -> enumerate
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
index = 0
for user in member:
    if user[0] in ['A', 'a']:
        member[index] = 0
    index += 1 
print(member)

# 기대 : ['Spencer',0 ,0 , 'Chen', 'John',0 ,0 , 'Darby']
# 실제 : ['Spencer', 0, 0, 'Chen', 'John', 0, 0, 'Darby']