import sys
from collections import deque
input = sys.stdin.readline

N, M, F = map(int, input().split())
board = [[1] * (N + 1)] + [[1] + list(map(int, input().split())) for _ in range(N)]
sy, sx = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
global fuel
fuel = F


# bfs로 직접 거리를 구해야함
def find_shortest_guest(sy, sx, infos):
    visited = [[-1] * (N + 1) for _ in range(N + 1)]
    visited[sy][sx] = 0
    queue = deque([(sy, sx)])
    while queue:
        y, x= queue.popleft()
        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny > N or nx < 0 or nx > N:
                continue
            if board[ny][nx] == 1 or visited[ny][nx] != -1:
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))
    
    gy, gx, ey, ex, idx = sy, sx, sy, sx, 0
    min_value = 1e15
    for i, (ay, ax, by, bx) in enumerate(infos):
        if visited[ay][ax] > min_value: continue
        elif visited[ay][ax] == min_value and ay > gy: continue
        elif visited[ay][ax] == min_value and ay == gy and ax > gx: continue
        gy, gx, ey, ex, idx = ay, ax, by, bx, i
        min_value = visited[ay][ax]
    del infos[idx]  
    return gy, gx, ey, ex
            

def move(sy, sx, gy, gx):
   
    if sy == gy and sx == gx:
        return 0
    
    queue = deque([(sy, sx)])
    visited = [[-1] * (N + 1) for _ in range(N + 1)]
    visited[sy][sx] = 0
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny > N or nx < 0 or nx > N:
                continue
            if board[ny][nx] == 1 or visited[ny][nx] != -1:
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))
            if ny == gy and nx == gx:
                return visited[ny][nx]
            
    return visited[gy][gx]
        
def charge_remained_fuel(used):
    if used < 0:
        return -1
    elif fuel - used < 0:
        return -1
    else:
        return fuel + used


while infos:
    gy, gx, ey, ex = find_shortest_guest(sy, sx, infos)
    used = move(sy, sx, gy, gx)
    if used < 0: 
        fuel = used
        break
    fuel -= used
    used = move(gy, gx, ey, ex)
    fuel = charge_remained_fuel(used)
    if fuel == -1: break
    sy, sx = ey, ex

print(fuel)