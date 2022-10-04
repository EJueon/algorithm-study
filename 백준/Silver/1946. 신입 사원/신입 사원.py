import sys 
input = sys.stdin.readline

test_num = int(input())

for n in range(test_num):
    p_count = int(input())
    p_list = []
    for c in range(p_count):
        M, K = map(int, input().split())
        p_list.append([M, K])
    p_list.sort()
    fail = 0
    p_max = p_count
    for p in p_list:
        if p[1] < p_max:
            p_max = p[1]
        elif p[1] > p_max:
            fail += 1
    print(f'{p_count - fail}')

            