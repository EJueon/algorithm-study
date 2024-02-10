import sys
from collections import deque
input = sys.stdin.readline

# 공기(0)를 중심으로 치즈 겉을 찾아서 제거 
R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(R, C, y, x):
    queue = deque([(y, x)])
    visited = [[0] * C for _ in range(R)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if visited[ny][nx] == 1:
                continue
            if board[ny][nx] == 1: 
                board[ny][nx] = 0
            else:
                queue.append((ny, nx))
            visited[ny][nx] = 1
    
    return sum([sum(row) for row in board])


cheese_cnt = sum([sum(row) for row in board])

# 처음부터 cheese가 없는 경우 예외처리
if cheese_cnt == 0:
    print(0)
    print(0)
    
# cheese가 존재하는 경우
else:
    cheese_cnts = [cheese_cnt]
    while True:
        cnt = bfs(R, C, 0, 0)
        if cnt == 0:
            print(len(cheese_cnts))
            print(cheese_cnts[-1])
            break
        else:
            cheese_cnts.append(cnt)
