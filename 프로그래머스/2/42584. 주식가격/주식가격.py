from collections import deque


# 스택 사용 안한 버전
def solution(prices):
    answer = [0] * len(prices)
    
    for i, price in enumerate(prices):
        for sec in range(i + 1, len(prices)):
            answer[i] = sec - i
            if prices[i] > prices[sec]:
                break
    
    return answer

# 스택 사용한 버전
# def solution(prices):
#     answer = [0] * len(prices)
#     stack = deque() # price, idx가 포함됨
    
#     for i in range(len(prices)): # 초처럼 사용한듯
#         for p, idx in stack:
#             answer[idx] += 1
            
#         # 스택이 사용되는 부분. 해당 시간에 price를 비교. 
#         # 해당 로직때문에 stack에는 가장 상단이 가장 크다. 
#         while stack and stack[-1][0] > prices[i]:
#             stack.pop()
#         stack.append((prices[i], i))
#     return answer