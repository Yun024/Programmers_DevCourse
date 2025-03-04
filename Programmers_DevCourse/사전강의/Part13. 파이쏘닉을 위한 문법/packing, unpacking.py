# * unpacking
nums1 = [1, 3, 5, 7, 9, 11]
nums2 = [1, 3, 5, 7, 9, 11]

## *와 대괄호가 만나면 벗겨냄
print(*nums1)
print(1, 3, 5, 7, 9, 11)

# 리스트를 합친다.
## nums1.extend(nums2) 파괴적
new_nums = nums1 + nums2
print(new_nums)
new_nums = [*nums1, *nums2]
print(new_nums)

dict1 = {'spencer': 100, 'mussg': 20}
dict2 = {'may': 30, 'allen': 15}
## dict1.update(dict2): 파괴적
## print(dict1)

new_dict = {**dict1, **dict2} # 바파괴적
print(new_dict)