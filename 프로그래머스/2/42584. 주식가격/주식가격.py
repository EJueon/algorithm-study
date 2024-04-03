'''
규칙
    1.  초단위로 기록된 주식가격
    2. 해당 주식가격보다 작을 때 떨어졌다고 함.

로직
    1. prices를 deque로 만든다.
    2. prices가 없어질 때까지 반복한다.
        1. last = popleft()를 하고
        * count 초기화
        2. 나머지 prices와 last를 비교한다. (for문 사용)
            3. 해당 주식가격보다 작을 경우, count를 멈춘다.
            4. 아닐 경우 count를 추가한다.
        answer.append(count)를 한다.
'''
from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        last = prices.popleft()
        cnt = 0
        for price in prices:
            cnt += 1
            if price < last:
                break
            
        answer.append(cnt)
    return answer