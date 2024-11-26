# *args **kwargs : 멀티 파라미터
def check_basket(*item) :
    print(f'장바구니 상황 : {item}') 
    # 반복문

# print(1, 2, 3, 4)
# check_basket('사과')
# check_basket('바나나')
# check_basket('폭탄')
# check_basket('폭탄', '파인애플')

## 애스터리스크가 하나 : 튜플로 입력 
check_basket('사과', '고기', '삶은계란')

## 애스터리스크 두개는 딕셔너리
# check_basket(breakfast='사과',lunch='고기',dinner='삶은계란')
{'breakfast': '사과', 'lunch': '고기', 'dinner': '삶은계란'} # dict

print() # 컨트롤 + 함수에 마우스 올리면 *기호 확인가능 