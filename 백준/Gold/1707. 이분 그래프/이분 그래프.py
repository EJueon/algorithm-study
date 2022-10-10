import sys 
input = sys.stdin.readline

from collections import deque   
def dfs(v, color, visited, graph):
    queue = deque()
    visited[v] = color
    queue.append((v, color))

    while queue:
        cur_v, cur_color = queue.popleft()
        
        for g_v in graph[cur_v]:
            if not visited[g_v]:
                queue.append((g_v, -cur_color))
                visited[g_v] = -cur_color
            elif visited[cur_v] == visited[g_v]:
                return False
    return True

#입력
N = int(input())
ret = None
for _ in range(N):
    V_cnt, E_cnt = map(int, input().split())
    graph = [[] for _ in range(V_cnt + 1)]
    visited = [0] * (V_cnt + 1)
    
    for _ in range(E_cnt):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for v in range(1, v+1):
        if not visited[v]:
            ret = dfs(v, 1, visited, graph)
            if not ret: 
                break
    print('YES') if ret else print('NO')


    
    