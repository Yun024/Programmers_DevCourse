def solution(L, x):
    answer = []
    [answer.append(j) for j,i in enumerate(L) if i == x]
    return [-1] if len(answer) == 0 else answer