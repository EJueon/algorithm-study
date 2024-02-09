def solution(s, n):
    
    answer = []
    for alpha in s:
        
        # 공백 제약조건 처리
        if alpha == " ": 
            answer.append(" ")
            continue
            
        start_num = ord('A') if alpha.isupper() else ord('a')
        answer.append(chr((ord(alpha) + n - start_num) % 26 + start_num))
        
        
    return ''.join(answer)