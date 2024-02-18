import sys
from collections import deque
input = sys.stdin.readline

Y = 12
X = 6
board = [list(*input().split()) for _ in range(Y)]
DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))

board_q = []
for x in range(X):
    queue = []
    for y in range(Y):
        queue.append(board[y][x])
    board_q.append(queue)
    
board = board_q

def find_same(board, visited, x, y):
    # bfs
    queue = deque()
    queue.append((x, y))
    color = board[x][y]
    visited[x][y] = 1
    sames = []
    
    while queue:
        x, y = queue.popleft()
        sames.append((x, y))
        
        for dx, dy in DELTAS:
            nx = x + dx
            ny = y + dy
            if ny < 0 or ny >= Y or nx < 0 or nx >= X:
                continue
            if visited[nx][ny] == 0 and board[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = 1        
    return sames

def pop(board, stacks):
    for x, y in stack:
        board[x][y] = '.'
    return 1

def down(board):
    new_board = []
    for col in board:
        stack = deque()

        for c in col:
            if c != '.':
                stack.append(c)
        
        for _ in range(Y - len(stack)):
            stack.appendleft('.')
            
        new_board.append(list(stack))
    return new_board


total_cnt = 0
while True:
    visited = [[0] * Y for _ in range(X)]
    stack = []
    for x in range(X):
        for y in range(Y):
            if board[x][y] != '.':
                temp_stack = find_same(board, visited, x, y)
                if len(temp_stack) >= 4:
                    stack.extend(temp_stack)

    if not stack: break
    total_cnt += pop(board, stack)
    board = down(board)
    # print(board)

print(total_cnt)
