import sys
from collections import deque
input = sys.stdin.readline

HDELTAS = ((-2, 1), (-1, 2), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2))
MDELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
MAX_VALUE = 1e5
visited = [[[MAX_VALUE] * (K + 1) for _ in range(W)] for _ in range(H)]

def search(board, visited, ny, nx, y, x, k):
    if ny >= H or ny < 0 or nx >= W or nx < 0 or board[ny][nx] == 1:
        return False
    
    return True

def bfs(board, visited, K):
    queue = deque([(0, 0, K)]) # y, x, k
    visited[0][0][K] = 0
    
    while queue:
        y, x, k = queue.popleft()
        if y == H-1 and x == W-1: break
        if k > 0:
            for dy, dx in HDELTAS:
                ny, nx = y + dy, x + dx
                if not search(board, visited, ny, nx, y, x, k):
                    continue
                if visited[ny][nx][k-1] <= visited[y][x][k] + 1:
                    continue
                visited[ny][nx][k-1] = visited[y][x][k] + 1
                queue.append((ny, nx, k-1))
        
        for dy, dx in MDELTAS:
            ny, nx = y + dy, x + dx
            if not search(board, visited, ny, nx, y, x, k):
                continue
            if visited[ny][nx][k] <= visited[y][x][k] + 1:
                continue
            visited[ny][nx][k] = visited[y][x][k] + 1
            queue.append((ny, nx, k))

    return visited[H-1][W-1][k]

answer = bfs(board, visited, K)
print(answer if answer is not MAX_VALUE else -1)