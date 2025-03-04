# Conditional Breakpoint
for x in range(100):
    print(x)

## 중단점 편집[식] + 적중횟수[3]
## 브레이크 포인트를 여러개 걸 수 있음

member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']

for user in member.copy():
    if user[0] in ['A', 'a']:
        member.remove(user)
print(member)

## 중단점[적중횟수] : 입력한 횟수에서 반복문 멈춤 

member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']

for user in member.copy():
    if user[0] in ['A', 'a']:
        member.remove(user)
        # print(f'현재 member : {member}')
print(member)

## 로그포인트: print를 python과 상관없이 vscode에서 출력해줌/디버그 콘솔
