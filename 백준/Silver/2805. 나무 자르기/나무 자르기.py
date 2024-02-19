import sys
input = sys.stdin.readline

N, goal = map(int, input().split())
trees = list(map(int, input().split()))

def solution(trees, goal):
    answer = 0
    
    # 절단기 높이 기준
    start, end = 0, max(trees)
    
    
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for tree in trees:
            if tree - mid > 0:
                total += (tree - mid)
            if total >= goal:
                answer = mid
                break
        
        if total >= goal:
            start = mid + 1
        else:
            end = mid - 1
            
    return answer

print(solution(trees, goal))