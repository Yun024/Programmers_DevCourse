# match_case.py 3.10~
# switch/case문
status = 404

match status:
    case 200:
        print(f"{status} Success")
    case 300:
        print(f"{status} Redirect")
    case 400:
        print(f"{status} Client Error")
    case 500:
        print(f"{status} Server Error")
    case _:  # 와일드카드 케이스는 맨 아래에 배치해야함
        print(f"{status} 해당사항이 없습니다.")

### 와일드카드 : 아무것도 해당사항이 없을 때(default)
### 오른쪽에 있는게 단독적인 데이터일 때 사용가능

# python version 확인 방법
import os
os.system("python --version")