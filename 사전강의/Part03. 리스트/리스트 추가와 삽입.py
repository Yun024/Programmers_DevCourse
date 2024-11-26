# list append insert
# index, valueh(element) -> item
# append : 추가
# insert : 삽입 
user1 = ['Spencer', '200']
user2 = ['Mussg', '50']

# 추가
user1.append(100) # 파괴적
user2 = user2 + [150,] # 비파괴적
print(user1,user2)

# 추가
user1.append([1.0, 0.8])
user2 = user2 + [[1.0, 0.8],1,[2,3,4,[5,6,7]]] 
## 중첩 리스트, 이차원 리스트, 이중 리스트
print(user1[3], user2[3])

# 삽입
user1 = ['Spencer', '200']
user2 = ['Mussg', '50']
user1.insert(1, 100)
user2.insert(100,150) # 범위가 넘어갈 경우 맨 뒷자리 
print(user2)
