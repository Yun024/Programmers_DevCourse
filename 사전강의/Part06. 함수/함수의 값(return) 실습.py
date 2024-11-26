## return은 실행되면 함수는 종료 
## return 아래에 있는 코드는 쓰레기 코드 = 실행되지 않음 

def purchase_price(price, sale_per):
    new_price = int(price * (100 - sale_per) / 100)
    # print(f"구매 가격은 {new_price}원 입니다.") 
    return new_price


p1 = purchase_price(20000,50)
p2 = purchase_price(40000,20)
print(p1,p2)
print(p1 + p2)