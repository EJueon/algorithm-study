import sys
from collections import deque
input = sys.stdin.readline

def process(P, arr):
    r_flag = False
    queue = deque(arr)
    try:
        for p in P:
            if p == 'R':
                # reverse 하는 process는 시간복잡도가 O(n)이므로 가장 마지막에 수행
                r_flag = not r_flag
            elif p == 'D':
                if not r_flag:
                    queue.popleft()
                else:
                    queue.pop()
    except:
        return "error"
    
    arr = list(queue)
    if r_flag:
        arr = reversed(arr)
        
    return f"[{','.join(list(map(str, arr)))}]"

T = int(input())
for _ in range(T):
    P = list(input())
    n = int(input())
    # str to int array
    arr = input().split('\n')[0][1:-1].split(',')
    if '' in arr and len(arr) == 1:
        arr = []
    else:
        arr = list(map(int, arr))
    print(process(P, arr))
