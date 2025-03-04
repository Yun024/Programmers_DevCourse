# enumerate()
rainbow = ['red', 'orange', 'yullow', 'green', 'blue', 'navy', 'purple']
## 0번째 색은 red
## 1번째 색은 orange

index = 0
for color in rainbow:
    print(f'{index+1}번째 색깔은 {color}')
    index +=1 

# print(list(enumerate(rainbow)))
for index, color in enumerate(rainbow):
    print(f'{index+1}번째 색깔은 {color}')