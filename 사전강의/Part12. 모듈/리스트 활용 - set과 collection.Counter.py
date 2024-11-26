nums = [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6]
basket = ['banana', 'banana', 'banana', 'apple', 'melon']

# set() 중복 데이터를 담을 수 없음, 인덱스 없음 
print(set(nums))
print(list(set(nums))[0])

# collections Counter
from collections import Counter
print(Counter(nums))
print(Counter(basket)['banana'])
new_basket = dict(Counter(basket))
print(new_basket)

text = 'fasdlfjsdalkjfsdalkthlkasdfhalsdkfn'
print(Counter(text).most_common(2)) ## 인자: 2-> 두번째까지
new_text = Counter(text)
print(new_text)