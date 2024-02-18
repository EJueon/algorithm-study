import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def count_iceberg(icebergs):
    visited = [[0] * M for _ in range(N)]
    total_cnt = 0
    
    for y, x in icebergs:
        stack = deque()
        if visited[y][x] == 0:
            total_cnt += 1
            stack.append((y, x))
            visited[y][x] = total_cnt
            while stack:
                y, x = stack.pop()
                for dy, dx in DELTAS:
                    ny = y + dy
                    nx = x + dx
                    if ny < 0 or ny >= N or nx < 0 or nx >= M:
                        continue
                    if board[ny][nx] > 0 and visited[ny][nx] == 0:
                        visited[ny][nx] = total_cnt
                        stack.append((ny, nx))
    return total_cnt



def melt_ice(board, visited): 
    icebergs = []
    for y in range(N):
        for x in range(M):
            if visited[y][x] > 0:
                board[y][x] =  board[y][x] - visited[y][x] if board[y][x] > visited[y][x] else 0
            if board[y][x] > 0:
                icebergs.append((y, x))
    return icebergs

def bfs(board, visited, y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = -1
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if board[ny][nx] > 0:
                visited[ny][nx] += 1
            elif board[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = -1
                queue.append((ny, nx))

def solution():
    time = 0
    while True:
        time += 1
        visited = [[0] * M for _ in range(N)]

        for y in range(N):
            for x in range(M):
                if board[y][x] == 0 and visited[y][x] == 0:            
                    bfs(board, visited, y, x)

        icebergs = melt_ice(board, visited)
        if len(icebergs) == 0: return 0
        if count_iceberg(icebergs) >= 2:
            return time
print(solution())
    