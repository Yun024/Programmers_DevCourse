# # for문
# def solution(x):
#     ans = 0
#     answer = [0,1]
#     if x < 2:
#         return answer[x]
#     else:
#         for i in range(x+1):
#             if i>= 2:
#                 answer.append(answer[i-1] + answer[i-2])
#     return answer[-1]

## 재귀함수
def solution(x) :
    if x < 2:
        return x 
    else:
        return solution(x-1) + solution(x-2)