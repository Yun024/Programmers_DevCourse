### Index함수 사용
# def solution(L, x):
#     try: 
#         return L.index(x)
#     except:
#         return -1

### 선형 탐색
# def solution(L,x):
#     for i in range(len(L)):
#         if L[i] == x:
#             return i
#     return -1
        
## 이진 탐색
def solution(L,x):
    lower = 0
    upper = len(L) -1
    while lower <= upper:
        middle = (lower + upper) //2 
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            lower = middle +1
        else: 
            upper = middle -1 
    return -1