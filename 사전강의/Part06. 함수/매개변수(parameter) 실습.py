# 삼각형 넓이 Define Function
def calc_triangle(width,height):
    area = width * height / 2
    print(f"삼각형의 넓이는 {area}입니다.")

## 함수 실행
calc_triangle(3,4)
calc_triangle(10,20)
calc_triangle(100,200)

## argument = 인자

# 아침 인사 함수 정의
def to_greeting(user):
    print("안녕하세요")
    print(f"오랜만이네요~ {user}")
    print("오늘 좋은 하루 되길 바라요~")

## 함수 실행
to_greeting("스펜서")
to_greeting("머쓱이")

# 쇼핑몰 할인율 -> 구매가격
def purchase_price(price, sale_per):
    new_price = int(price * (100 - sale_per) / 100)
    print(f"구매 가격은 {new_price}원 입니다.")

purchase_price(20000,50)
purchase_price(40000,20)