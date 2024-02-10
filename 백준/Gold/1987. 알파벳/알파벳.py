# https://www.acmicpc.net/problem/1987
# https://leeingyun96.tistory.com/22 참고

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))
max_cnt = 0
        
def dfs(y, x):
    global max_cnt
    queue = set()
    queue.add((y, x, board[y][x]))
    while queue:
        y, x, alphabets = queue.pop()
        max_cnt = max(max_cnt, len(alphabets))
        if max_cnt == 26: return max_cnt
        
        for dy, dx in DELTAS:
            ny = y + dy
            nx = x + dx
            # board 가로세로 길이 제약 조건
            if ny >= R or ny < 0 or nx >= C or nx < 0:
                continue
            # 알파벳 중복 
            if board[ny][nx] in set(alphabets):
                continue
            queue.add((ny, nx, alphabets + board[ny][nx]))    

dfs(0, 0)
print(max_cnt)