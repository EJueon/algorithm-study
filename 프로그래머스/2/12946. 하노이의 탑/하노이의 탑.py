# hanoi 법칙
# 마지막이 아닌 경우에는 모두 중간이 최종 종착지로 옮겨야 함
# 마지막인 


def hanoi(n, start, mid, end, answer):
    if n == 1:
        return answer.append([start, end])
    
    hanoi(n-1, start, end, mid, answer)
    answer.append([start, end])
    hanoi(n-1, mid, start, end, answer)


def solution(n):    
    answer = []
    hanoi(n, 1, 2, 3, answer)
    
    return answer