# list comprehension
## y = x**2
xs = list(range(0, 100))

## case1
ys1 = []
for x in xs:
    ys1.append(x**2)

## case2 
ys2 = [x**2 for x in xs]
print(ys1 == ys2)

ys3 = [f'x는 {x}, y는 {x**2}' for x in xs]
print(ys3)

ys4 = [(x,x**2) for x in xs]
print(ys4)