import sys
input = sys.stdin.readline

N, M = map(int, input().split())
order_arr = [0] * (2 * N - 1)
for _ in range(M):
    o1, o2, o3 = map(int, input().split())
    for i in range(o1, o1 + o2):
        order_arr[i] += 1
    for i in range(o1 + o2, 2 * N - 1):
        order_arr[i] += 2

board = [[1] * N for _ in range(N)]

def print_board(board):
    for row in board:
        print(' '.join(list(map(str, row))))
    
def grow_by_orders(N, board, order_arr):
    cnt = 0
    # 열 배당
    for i in range(N-1, -1, -1):
        board[i][0] += order_arr[cnt]
        cnt += 1
        
    for i in range(1, N):
        board[0][i] += order_arr[cnt]
        cnt += 1

def grow_relative(N, board):
    for y in range(1, N):
        for x in range(1, N):
            # check L D U
            board[y][x] = board[0][x]
    
final_order = [0, 0, 0]      
grow_by_orders(N, board, order_arr)
grow_relative(N, board)
    

print_board(board)