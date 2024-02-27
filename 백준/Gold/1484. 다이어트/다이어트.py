import sys
import math
input = sys.stdin.readline

G = int(input())

def twopointer_search(G):
    
    left, right = 1, 1
    answers = []
    
    while left < 1e5 and right < 1e5:
        # G = A**2 - B**2 -> (A+B)(A-B)
        value = left ** 2 - right ** 2

        if value == G: answers.append(left)
        
        if value < G: left += 1
        else: right += 1
        
    if not answers: print(-1)
    else:
        for ans in answers: print(ans)
        
        
    
twopointer_search(G)