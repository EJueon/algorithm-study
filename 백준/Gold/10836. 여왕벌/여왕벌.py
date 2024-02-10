import sys
input = sys.stdin.readline

N, M = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(M)]
board = [[1] * N for _ in range(N)]

def change_std(order, std):
    while std < 2 and order[std] == 0:
        std += 1
    return std

def print_board(board):
    for row in board:
        print(' '.join(list(map(str, row))))
    

def grow_by_orders(N, board, order):
    std = 0
    # 열 배당
    
    for i in range(N-1, -1, -1):
        std = change_std(order, std)
        board[i][0] += std
        order[std] -= 1
        
    for i in range(1, N):
        std = change_std(order, std)
        board[0][i] += std
        order[std] -= 1

def grow_relative(N, board):
    for y in range(1, N):
        for x in range(1, N):
            # check L D U
            board[y][x] = max(board[y][x-1], board[y-1][x-1], board[y-1][x])
            
for order in orders:
    grow_by_orders(N, board, order)
grow_relative(N, board)
    

print_board(board)