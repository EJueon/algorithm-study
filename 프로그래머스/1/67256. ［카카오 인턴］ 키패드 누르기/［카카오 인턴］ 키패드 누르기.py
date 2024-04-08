DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))
board = {1: (0, 0), 2: (1, 0), 3: (2, 0), 
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2),
        '*': (0, 3), 0: (1, 3), '#': (2, 3)}
from collections import deque

def dist(start, dest):
    
    return abs(dest[1] - start[1]) + abs(dest[0] - start[0])

def solution(numbers, hand):
    answers = []
    L_cur, R_cur = board['*'], board['#']
    for num in numbers:
        if num in [1, 4, 7]:
            answers.append('L')
            L_cur = board[num]
        elif num in [3, 6, 9]:
            answers.append('R')
            R_cur = board[num]
        elif num in [2, 5, 8, 0]:
            L_dist = dist(L_cur, board[num])
            R_dist = dist(R_cur, board[num])
            if L_dist < R_dist or (L_dist == R_dist and hand == 'left'):
                answers.append('L')
                L_cur = board[num]
            elif L_dist > R_dist or (L_dist == R_dist and hand == 'right'):
                answers.append('R')
                R_cur = board[num]
                    
    return ''.join(answers)
        

