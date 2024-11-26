member  = ['Spencer', 'Mussg', 'Allen', 'Chen', 'John', 'May']
theif = "Allen"

for person in member:
    print(person)
    if person == theif:
        print("도둑이야!")
        print("당신은 변호사를 선임할 수 있으며...")
        break


print("검문이 끝났습니다.")