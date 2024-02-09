from itertools import combinations
def solution(numbers):
    answer = set()
    numbers = list(combinations(numbers, 2))
    for n1, n2 in numbers:
        answer.add(n1 + n2)
        
    return sorted(answer)
