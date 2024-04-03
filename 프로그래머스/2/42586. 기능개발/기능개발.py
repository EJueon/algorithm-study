'''

'''
from collections import deque
from math import ceil
def solution(progresses, speeds):
    queue = deque(ceil((100 - p) / s) for p, s in zip(progresses, speeds))
    cur_time = 0 
    answer = []
    top = -1
    
    while queue:
        finished = queue.popleft() 
        if cur_time >= finished:
            answer[top] += 1
        else:
            cur_time = finished 
            answer.append(1)
            top += 1
        
    
    return answer