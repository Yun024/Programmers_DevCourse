#list slice -> Non-destructive 
nums =[33,22,11,77,55,66,99,88]
print(nums[2:6])
print(nums[6:2])
print(nums[-2:-6])
print(nums[-6:-2])

# 앞(0) 뒷(맨마지막) 생략
print(nums[:6])
print(nums[2:])

# step
nums =[33,22,11,77,55,66,99,88]
print(nums[2:7])
print(nums[2:7:2])
print(nums[2:7:3])
print(nums[6:2:-1])
print(nums[-2:-6:-1])

# adv slice
nums = [33,22,11,77,55,66,99,88]
print(nums[:])
print(nums[::-1])
new_nums = nums[::-1]
print(new_nums)