import sys
from collections import deque
input = sys.stdin.readline

DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))

def bfs(board, visited, y, x, cnt):
    queue = deque([(y, x)])
    while queue:
        y, x = queue.pop()
        
        for dy, dx in DELTAS:
            ny = y + dy
            nx = x + dx 
            if ny >= H or ny < 0 or nx >= W or nx < 0:
                continue
            if board[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = cnt
                queue.append((ny, nx))


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    
    board = []
    for h in range(H):
        board.append(list(map(int, input().split())))
    
    
    visited = [[0] * W for _ in range(H)]
    cnt = 0
    for h in range(H):
        for w in range(W):
            if board[h][w] == 1 and visited[h][w] == 0:
                cnt += 1
                visited[h][w] = cnt
                bfs(board, visited, h, w, cnt)
                
    print(cnt)