import sys
from collections import deque
input = sys.stdin.readline

DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))
R, C = map(int, input().split())
board = [list(input().split()[0]) for _ in range(R)]
visited = [[-1] * C for _ in range(R)]
w_visited = [[-1] * C for _ in range(R)] # water visited
START, END, WATERS = None, None, deque()

# 물은 매분마다 인접한 비어있는 칸으로 확장함 
def add_waters(board, waters, visited):
    # bfs
    queue = deque(waters)
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
               continue
            if board[ny][nx] in ('X', 'D') or visited[ny][nx] > -1:
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))


def move(board, visited, start, end, w_visited):
    # bfs
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in DELTAS:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
               continue
            if board[ny][nx] in ['X', '*'] or visited[ny][nx] > -1: 
               continue
            # w_visited 로 언제 물이 확장되었는지 확인. 이때 -1로 초기화 하였기 때문에 예외처리
            if visited[y][x] + 1 >= w_visited[ny][nx] and w_visited[ny][nx] != -1:
                continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))
            if ny == end[0] and nx == end[1]:
                return visited[end[0]][end[1]]
    return visited[end[0]][end[1]] 
           
# 초기화 
for y in range(R):
    for x in range(C):
        if board[y][x] == 'D':
            END = (y, x)
        elif board[y][x] == 'S':
            START = (y, x)
        elif board[y][x] == '*':
            WATERS.append((y, x))
            w_visited[y][x] = 0
            
add_waters(board, WATERS, w_visited)
answer = move(board, visited, START, END, w_visited)
if answer == -1:
    print("KAKTUS")
else:
    print(answer)
