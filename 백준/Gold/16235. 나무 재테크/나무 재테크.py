import sys
from itertools import chain
from collections import defaultdict, deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[-1] * (N + 1)] + [[-1] + [5] * N for _ in range(N)]
A = [[-1] * (N + 1)] + [[-1] + list(map(int, input().split())) for _ in range(N)]
infos = [list(map(int, input().split())) for _ in range(M)] # x, y, z
trees = defaultdict(deque)
DELTAS = ((-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def spring_summer(board, trees):
    for (x, y), tree in trees.items():
        new_tree = deque()

        while tree:
            age = tree[0]
            if board[x][y] >= age:
                board[x][y] -= age
                tree.popleft()
                new_tree.append(age + 1)
            else:
                board[x][y] += sum([t // 2 for t in tree])
                break

        trees[(x, y)] = new_tree

def fall_winter(trees):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            tree = trees.get((x, y))
    
            if not tree: 
                board[x][y] += A[x][y]
                continue
            
            for i in range(len(tree)):
                if tree[i] % 5 == 0:
                    for dy, dx in DELTAS:
                        ny, nx = y + dy, x + dx
                        if ny <= 0 or ny > N or nx <= 0 or nx > N:
                            continue
                        trees[(nx, ny)].appendleft(1)
            board[x][y] += A[x][y]
                    

def count_trees(trees):
    cnt = 0
    for tree in trees.values():
        cnt += len(tree)
    return cnt

for x, y, z in infos:
    trees[(x, y)].append(z)

for k in range(K):
    spring_summer(board, trees)
    fall_winter(trees)

print(count_trees(trees))
