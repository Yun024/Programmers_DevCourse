# list func
# sort() / 파괴적함수
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort()
print(nums)

# sort(reverse=True)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort(reverse=True)
print(nums)

# .reverse()
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.reverse()
print(nums)

# .remove(v) value
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
nums.remove(11) # 중복값일 경우 앞의 데이터만, 존재하지 않을 경우 에러 발생
print(nums)

# .index(v)
nums = [33, 22, 11, 77, 55, 66, 99, 88]
idx = nums.index(11)
print(idx)

# .extend(v)
nums1 = [33, 22, 11, 77]
nums2 = [55, 66, 99, 88]
nums1.extend(nums2)
print(nums1)

nums1 = [33, 22, 11, 77]
nums2 = [55, 66, 99, 88]
nums3 = nums1 + nums2
print(nums3)

# .count(v)
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
cnt = nums.count(11)
print(cnt)

# .pop(i) default값은 맨뒤
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
num = nums.pop() # del nums[1] -> None , pop은 뽑아낸다 
print(num)

# len()
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
print(len(nums))

# sorted(v), sorted(v, reverse=True) / 비파괴적함수
nums = [33, 22, 11, 77, 55, 66, 11, 99, 88]
print(sorted(nums))


