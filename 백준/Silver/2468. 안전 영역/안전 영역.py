# 입력
# import sys 
from collections import deque
# input = sys.stdin.readline
N = int(input())
area = []
max_h = 0
for col in range(N):
    row = list(map(int, input().split()))
    for r in row:
        if r > max_h:
            max_h = r
    area.append(row)
# 문제풀이  
DELTAS = ((0,1), (0,-1), (1,0), (-1,0))

def dfs(y, x, std, visited):
    
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx
            # if ny < 0 or ny >= N or nx < 0 or nx >= N:
                # continue
            if 0 <= ny < N and 0 <= nx < N:
                if area[ny][nx] > std and visited[ny][nx]==0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

ans = 0
for std in range(max_h):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j] > std and visited[i][j]==0:
                dfs(i, j, std, visited)
                cnt += 1      
    if ans < cnt:
        ans = cnt
print(ans)


