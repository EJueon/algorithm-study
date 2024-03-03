import sys
from collections import deque
input = sys.stdin.readline
# DP가 주이고 재귀 dfs를 달고다니는 DP라고 보면 됨 
# 1937 욕심쟁이 판다도 참고하자 

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited = [[-1] * N for _ in range(M)]

def dfs(board, visited, y, x):
    
    if x == N - 1 and y == M - 1:
        return 1
    
    if visited[y][x] != -1:
        return visited[y][x]
    
    cnt = 0
    for dy, dx in DELTAS:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= M or nx < 0 or nx >= N:
            continue
        if board[ny][nx] < board[y][x]:
            cnt += dfs(board, visited, ny, nx)
    
    visited[y][x] = cnt
    return visited[y][x]

# dfs는 0,0 -> M, M으로 가지만 dp는 M, N -> 0,0으로 이동하는 구조
print(dfs(board, visited, 0, 0))

    