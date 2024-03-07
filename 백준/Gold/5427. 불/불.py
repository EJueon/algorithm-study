import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def expand_fire(board, f_visited, fires, H, W):
    # bfs
    queue = deque(fires)
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            elif board[ny][nx] == '#' or f_visited[ny][nx] != -1:
                continue
            f_visited[ny][nx] = f_visited[y][x] + 1
            queue.append((ny, nx))

def move(board, visited, f_visited, start, ends, H, W):
    # bfs
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            elif board[ny][nx] == '#' or visited[ny][nx] != -1:
                continue
            elif f_visited[ny][nx] > 0 and visited[y][x] + 1 >= f_visited[ny][nx]:
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny,nx))
            
    time = 1e7
    for ey, ex in ends:
        if visited[ey][ex] < time and visited[ey][ex] != -1:
            time = visited[ey][ex]
    
    return time if time < 1e7 else -1
    

def solution():
    
    W, H = map(int, input().split())
    board = [list(input().split()[0]) for _ in range(H)]
    f_visited = [[-1] * W for _ in range(H)]
    visited = [[-1] * W for _ in range(H)]
    START, ENDS, FIRES = None, list(), list()

    for y in range(H):
        for x in range(W):
            if board[y][x] == '@':
                START = (y, x)
            if (y == 0 or y == (H - 1) or x == 0 or x == (W - 1)) and (board[y][x] in ('.', '@')):
                if board[y][x] == '@': return 1
                ENDS.append((y, x))
            elif board[y][x] == '*':
                FIRES.append((y, x))
                f_visited[y][x] = 1
    if not ENDS:
        return 0

    expand_fire(board, f_visited, FIRES, H, W)
    return move(board, visited, f_visited, START, ENDS, H, W)
    
for _ in range(T):
    answer = solution()
    print(answer if answer > 0 else "IMPOSSIBLE")