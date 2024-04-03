def solution(phone_book):
    answer = True
    # 앞 배열의 번호길이가 가장 짧아져야 하므로 정렬 필수 
    phone_book.sort() 
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2[:len(p1)] == p1: # 또는 p2.startswith(p1)
            answer = False
            break
    
    return answer

