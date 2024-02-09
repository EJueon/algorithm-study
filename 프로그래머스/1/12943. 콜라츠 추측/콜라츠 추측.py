def collatz(num, cnt):
    
    # 1이 될 수 없는 수에 대한 제약 조건
    if cnt >= 500 and num != 1:
        return -1
    
    # 리턴 조건 
    if num == 1: return cnt
    
    # 재귀 
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    cnt = collatz(num, cnt+1)
    
    return cnt
    

def solution(num):
    return collatz(num, 0)