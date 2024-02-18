import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())

# parent 초기값은 자기 자신 !! 
parent = [i for i in range(N+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return 
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    inst, a, b = map(int, input().split())
    if inst == 0:
        union(parent, a, b)
    elif inst == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")