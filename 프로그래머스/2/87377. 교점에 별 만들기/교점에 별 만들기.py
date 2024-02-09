def solution(lines):
    
    positions = []
    
    # 최소한의 크기를 나타내기 위한 최솟값, 최댓값 설정
    x_min = y_min = int(1e15) 
    x_max = y_max = int(-1e15) 
    
    # 교점 판단 로직 
    for A, B, E in lines[:-1]:
        for C, D, F in lines[1:]:
            if A * D == B * C: continue
            x = ((B * F) - (E * D)) / ((A * D) - (B * C))
            y = ((E * C) - (A * F)) / ((A * D) - (B * C))
            
            # 교점중 정수 좌표만을 한정
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                positions.append([x, y])
                x_min = min(x, x_min)
                x_max = max(x, x_max)
                y_min = min(y, y_min)
                y_max = max(y, y_max)
    
    # 최소 길이의 리스트 생성
    coord = [['.'] * (x_max - x_min + 1) for _ in range(0, y_max - y_min + 1)]
    
    for x, y in positions:
        nx = x - x_min
        ny = y - y_min
        coord[ny][nx] = "*"
    
    answer = [''.join(c) for c in coord]
    
    # 리스트상으로는 1, 2 사분면이 더 크기 때문에 밑에 나오게 되므로 거꾸로 출력해야함. 
    return answer[::-1]
    
                