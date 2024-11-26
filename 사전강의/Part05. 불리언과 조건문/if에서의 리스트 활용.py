# if list, tuple, sequence - in 연산자
# case1 soccer, baseball, basketball
sport = 'tennis'

if sport == 'soccer' or sport == 'baseball' or sport =='basketball' :
    print("조사항목포함")
else:
    print("비조사항목")


# case2 list count
## count대신 index메소드를 사용하면 0번째에 있는 스포츠의 경우 False출력
sport = 'tennis'
check_sports = ['soccer', 'basketball', 'baseball']
if check_sports.count(sport) :
    print("조사항목포함")
else:
    print("비조사항목")

# case3 in 연산자
print(3 in [1,2,4])
sport = 'tennis'
check_sports = ['soccer', 'basketball', 'baseball']
if sport in check_sports:
    print("조사항목포함")
else:
    print("비조사항목")