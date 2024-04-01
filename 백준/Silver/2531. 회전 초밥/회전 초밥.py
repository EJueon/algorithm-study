import sys
from collections import deque, Counter
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
infos = [int(input()) for _ in range(N)]

max_value = 0
p1 = 0


queue = deque()
for i in range(p1, p1 + k):
    i = i % N
    queue.append(infos[i])
    
q_set = set(queue)
q_set.add(c)
max_value = len(q_set)

p1 += 1
while p1 < N:
    i = (p1 + k - 1) % N
    if max_value == d: break
    queue.popleft()
    queue.append(infos[i])
    
    q_set = set(queue)
    q_set.add(c)
    max_value = max(len(q_set), max_value)
    
   
    p1 += 1
print(max_value)
    