import heapq
cnt = int(input())
cards = [int(input()) for c in range(cnt)]
heapq.heapify(cards)
card_cnt = 0
while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    card_cnt += (card1 + card2)
    heapq.heappush(cards, card1 + card2)
print(card_cnt)