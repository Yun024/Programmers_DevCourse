# 아침 인사
user = "스펜서"
print("안녕하세요")
print(f"오랜만이네요~ {user}")
print("오늘 좋은 하루 되길 바라요~")

## 아침 인사 함수
def to_greeting():
    user = "스펜서"
    print("안녕하세요")
    print(f"오랜만이네요~ {user}")
    print("오늘 좋은 하루 되길 바라요~")

## 함수 실행
to_greeting()

# 삼각형 넓이
area = 10 * 8 / 2
print(f"삼각형의 넓이는 {area}입니다.")

## 함수 정의
def calc_triangle():
    area = 10 * 8 / 2
    print(f"삼각형의 넓이는 {area}입니다.")

## 함수 실행
calc_triangle()

# 함수는 대부분 코드 윗부분에서 정의됨
## 함수 정의 영역
## 메인 코드 실행 영역
