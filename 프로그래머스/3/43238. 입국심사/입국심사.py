def solution(n, times):
    answer = 0
    
    start, end = 0, max(times) * n
    while start <= end:
        
        mid = (start + end) // 2
        processed_cnt = 0
        
        for time in times:
            processed_cnt += mid // time
            if processed_cnt >= n:
                break
        
        if processed_cnt >= n: 
            # 해당 시간이 충분히 모든 사람을 커버할 경우 최소 시간을 구해야함
            answer = mid
            end = mid - 1
        else:
            # 해당 시간이 모든 사람을 처리하는 데 충분하지 않음
            start = mid + 1
            
    return answer