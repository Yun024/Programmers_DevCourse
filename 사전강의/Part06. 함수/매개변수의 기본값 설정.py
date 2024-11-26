# 이미 살펴본 파라미터 기본값 지정
def teleport(x=0, y=0, z=1):
    print(f'텔레포트! {x}, {y}, {z}')

## 기본 값을 쓰는 파라미터는 뒤에 배치
## teleport(200)을 실행하는 경우 x, y에서 헷갈릴 수 있음 
teleport(100, 200, 5)
teleport(100, 200)
teleport(200)
teleport()
teleport(z=999)
teleport(z=999, x=50)

## 위치 에너지 mgh 지구 : 9.807m/s² 화성:3.721m/s² 달:1.62m/s²
def potential_energy(mass, height, gravity=9.8 ):
    return mass * gravity * height

print(potential_energy(100,20))
print(potential_energy(100,20,0.5))

## 멤버십이 처음에는 Bronze
def user(name, email, membership="Bronze"):
    print(f"가입완료 {name} {email} {membership}")

user("스펜서", "spencer@grepp.co")
number = 3 

## 매개변수 기본값 지정할때는 띄어쓰기 하지 않음 , 대입할때는 띄어씀
## 가독성때문 