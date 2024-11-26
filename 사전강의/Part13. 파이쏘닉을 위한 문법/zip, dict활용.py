users = ['Spencer', 'Mussg', 'John', 'Allen']
ages = [100, 20, 40, 70]

new_list = list(zip(users,ages))
print(new_list)
print(dict(new_list))

# dict comprehension
new_dict = {k:v-1 for k,v in zip(users,ages)}
print(new_dict)

xs = [3, 5, 7 ,8]
ys = [2, 5, 8, 4]
zs = [0, 1, 3, 6]
for x, y, z in zip(xs, ys, zs):
    print(f'{x} * {y} * {z} = {x*y*z}')


cars = [
    ('삼각형차', 90),
    ('표범차', 150),
    ('황소차', 200),
    ('왕관차', 120),
    ('말차', 180)
]

v1, v2 = zip(*cars)
print(v1, v2)

dict_cars = dict(cars)
print(dict_cars.keys(), dict_cars.values())


cars = [
    ('삼각형차', 90, 'KR'),
    ('표범차', 150, 'JP'),
    ('황소차', 200, 'EN'),
    ('왕관차', 120, 'US'),
    ('말차', 180, 'DE')
]
v1, v2, v3 = zip(*cars)
print(v1, v2, v3)