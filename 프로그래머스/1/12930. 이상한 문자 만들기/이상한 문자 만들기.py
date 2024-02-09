def solution(s):
    # 공백 기준 단어 구분
    words = s.split(' ')
    
    answer = ''
    
    # 각 단어의 문자별 소문자/대문자 처리 
    for word in words:
        for i, c in enumerate(word):
            if i % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '
        
    return answer[:-1]