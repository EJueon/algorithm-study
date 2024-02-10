import sys
from collections import deque
input = sys.stdin.readline

DELTAS = ((2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2))


def dfs(N, y, x, gy, gx):
    queue = deque([(y, x, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    answer = 1e15
    while queue:
        y, x, cnt = queue.popleft()
        for dy, dx in DELTAS:
            ny = y + dy
            nx = x + dx 
            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue
            if visited[ny][nx] == 1:
                continue
            if ny == gy and nx == gx:
                answer = min(answer, cnt+1)
                continue
            if cnt + 1 < answer:
                visited[ny][nx] = 1
                queue.append((ny, nx, cnt+1))

    return answer


T = int(input())
for _ in range(T):
    N = int(input())
    y, x = map(int, input().split())
    gy, gx = map(int, input().split())
    if y == gy and x == gx:
        print(0)
    else:
        print(dfs(N, y, x, gy, gx))
