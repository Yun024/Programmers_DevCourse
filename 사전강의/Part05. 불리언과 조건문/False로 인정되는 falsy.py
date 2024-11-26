# falsy - 없음, 비어있음, 0, 빈 리스트, 빈 문자열 
if True: 
    print("True")
else:
    print("False")

# case1 - 사용자 입력
username = input("Enter yourname : ")

if username :
    print("환영합니다.")
else:
    print("입력을 제대로 안했습니다.")

# case2 - 장바구니
basket = ['사과', '복숭아', '수박']
if basket :
    print("주문 시작")
else:
    print("장바구니가 비어있습니다.")

if not basket:
    print("장바구니가 비어있습니다.")