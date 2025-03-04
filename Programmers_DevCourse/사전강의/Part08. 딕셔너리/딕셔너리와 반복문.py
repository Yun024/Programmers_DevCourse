basket = {
    'apple': 3,
    'banana': 4,
    'pineapple': 5,
    'orange': 6
}

# case1
for item in basket:
    print(item)
    print(f'{item}는 {basket[item]}개 있습니다.')

# case2
for key,value in basket.items():
    print(key,value)
    print(f'{key}는 {value}개 있습니다.')

member = [
    {'name': 'Spencer', 'colleage': '프로그래머스', 'year': 20,
     'lang': 'Python'},
     {'name': 'Mussg', 'colleage': '프로그래머스', 'year': 20,
     'lang': 'C++'},
     {'name': 'John', 'colleage': '프로그래머스', 'year': 20,
     'lang': 'Java'},
     {'name': 'Allen', 'colleage': '프로그래머스', 'year': 20,
     'lang': 'Scratch'},
     {'name': 'Chen', 'colleage': '프로그래머스', 'year': 20,
     'lang': 'HTML'},
]

for user in member:
    if user['lang'] == 'Java':
        print(user)


    