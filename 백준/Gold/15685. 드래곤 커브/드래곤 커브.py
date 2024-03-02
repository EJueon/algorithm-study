import sys
from collections import deque
input = sys.stdin.readline

# 세대는 2**n 개의 선분으로 늘어나게 된다!!!
# x, y, d, g
N = int(input())
infos = [map(int, input().split()) for _ in range(N)]

# y, x
MAX_Y, MAX_X = 101, 101
DELTAS = ((0, 1), (-1, 0), (0, -1), (1, 0))
visited = [[0] * MAX_X for _ in range(MAX_Y)]

def rotate(d):
    return (d + 1) % 4

def draw_dragon(visited, x, y, d, g):
    visited[y][x] = 1 # initial point
    dy, dx = DELTAS[d]
    ny, nx, nd = y + dy, x + dx, d
    visited[ny][nx] = 1 # 0 세대 

    stack = deque([d])
    nstack = deque([d])
    for _ in range(g): # 1 ~ K 세대
        while stack:
            nd = rotate(stack.pop())
            dy, dx = DELTAS[nd]
            ny, nx = ny + dy, nx + dx
            visited[ny][nx] = 1
            nstack.append(nd)
        stack = nstack.copy()

def count_rects(visited):
    cnt = 0
    for y in range(MAX_Y - 1):
        for x in range(MAX_X - 1):
            if visited[y][x] and visited[y][x+1] and visited[y+1][x] and visited[y+1][x+1]:
                cnt += 1
    return cnt

for x, y, d, g in infos:
    draw_dragon(visited, x, y, d, g)
    
print(count_rects(visited))