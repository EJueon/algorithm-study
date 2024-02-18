import sys
from itertools import permutations
input = sys.stdin.readline

S = list(input().split()[0])
T = list(input().split()[0])

def add(s, x):
    return s + [x]

def op_1(s):
    return add(s, 'A')
    
def op_2(s):
    return add(s[::-1], 'B')

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