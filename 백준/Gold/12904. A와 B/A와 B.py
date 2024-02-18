from itertools import permutations
input = sys.stdin.readline

S = list(input().split()[0])
T = list(input().split()[0])

def solution(S, T):
    
    while len(T) != len(S):
        if T[-1] == 'A':
            T.pop()
        elif T[-1] == 'B':
            T.pop()
            T = T[::-1]
            
    if S == T:
        return 1
    else:
        return 0

print(solution(S, T))


# 도움 : https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-12904-A%EC%99%80-B
