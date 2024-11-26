# list
# create

numbers = [0, 1, 2, 3, 4]
chars = ['a', 'b', 'c', 'd']
users = ['Allen', 'Chen', 'John', 'May']
students = ['Allen', 170, 'Chen', 165, 'John', 180, 'May', 150]
# print(numbers, chars, users, students, sep ='\n')

# access, update -> index(자리번호) -> 0
print(numbers[4])
print(users[-1])
print(users)
users[-1] = 'Spencer'
print(users)

# delete -> index
del users[-1]
print(users)
del users[0]
print(users)

# del users;  print(users)
# a = 3 ; del a; print(a)