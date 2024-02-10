# https://www.acmicpc.net/problem/14719

import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
walls = list(map(int, input().split()))

board = []
for h in range(1, H+1):
    row = []
    for w in range(W):
        if h <= walls[w]:
            row.append(1)
        else:
            row.append(0)
    board.append(row)
    
def search(board, W, H):
    for y in range(H):
        stack = deque()
        flag = False
        for x in range(W):
            if board[y][x] == 1:
                if not flag: flag = True
                elif flag and stack: 
                    while stack:
                        wy, wx = stack.pop()
                        board[wy][wx] = 2
            elif flag:
                stack.append((y, x))


search(board, W, H)
print(sum([row.count(2) for row in board]))