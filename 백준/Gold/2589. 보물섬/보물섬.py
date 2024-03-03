import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().split()[0]) for _ in range(N)]
DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def find_max_value(visited):
    return max([max(v) for v in visited])

# 중복되지 않으면서 가장 긴 거리 
def search_max_distance(board, y, x):
    visited = [[-1] * M for _ in range(N)]
    queue = deque([(y, x)])
    visited[y][x] = 0
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx
            
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            elif board[ny][nx] == 'W': continue
            elif visited[ny][nx] != -1: continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))
    
    return find_max_value(visited)
        
answer = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == 'L':
            answer = max(answer, search_max_distance(board, y, x))
        
print(answer)