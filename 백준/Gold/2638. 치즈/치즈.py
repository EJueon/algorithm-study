import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def recover_board():
    for n in range(N):
        for m in range(M):
            if board[n][m] == 0.5:
                board[n][m] = 1
            else:
                board[n][m] = int(board[n][m])

def bfs(N, M, y, x):
    queue = deque([(y, x)])
    visited = [[0] * M for _ in range(N)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if board[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append((ny, nx))
            elif board[ny][nx] >0:
                board[ny][nx] -= 0.5
                visited[ny][nx] = 1
    recover_board()
    return sum([sum(row) for row in board])

if sum([sum(row) for row in board]) == 0:
    print(0)
else:
    cnt = 0
    while True:
        cheese_cnt = bfs(N, M, 0, 0)
        cnt += 1
        if cheese_cnt == 0:
            break
        
    print(cnt)