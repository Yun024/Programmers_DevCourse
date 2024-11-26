# 변수
store_name = '프로그래머스'
store_no = 200

# 할인가가 적용된 상품 가격 얻는 함수 
def purchase_price(price, sale_per):
    new_price = int(price * (100 - sale_per) / 100)
    new_price = int(new_price)
    # print(f"구매 가격은 {new_price}원 입니다.") 
    return new_price


# p1 = purchase_price(20000,50)
# p2 = purchase_price(40000,20)

# print(globals())


print(__name__)
## 실행이 어디서 되었느냐 : 해당 파일이 시작점일 경우 '__main__' 
## 외부에서 실행될 경우 파일 명 그래서 False

if __name__ =='__main__':
# 함수 실행
    print(purchase_price(20000,50))
    print(purchase_price(40000,20))