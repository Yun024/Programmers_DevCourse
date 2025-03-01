## sorted사용
# def solution(L, x):
#     L.append(x)
#     return sorted(L)

### for문 사용
def solution(L, x):
    for i in range(len(L)):
        if L[i] > x:
            L.insert(i,x)
            return L
    L.insert(i+1,x)
    return L