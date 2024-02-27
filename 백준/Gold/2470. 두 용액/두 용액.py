import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

def parameter_search(liquids):
    
    min_value = sys.maxsize
    p1, p2 = 0, 0
    start = 0
    end = len(liquids) - 1
    
    while start < end:
        value = abs(liquids[start] + liquids[end])
        
        if value < min_value:
            min_value = value
            p1 = start
            p2 = end
        
        if value == 0:
            break
    
        if liquids[start] + liquids[end] > 0:
            end -= 1
        else:
            start += 1
    return f"{liquids[p1]} {liquids[p2]}"

print(parameter_search(liquids))