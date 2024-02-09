def solution(answers):
    
    num_1 = (1, 2, 3, 4, 5)
    num_2 = (2, 1, 2, 3, 2, 4, 2, 5)
    num_3 = (3,3,1,1,2,2,4,4,5,5)
    students = [[0, 1], [0, 2], [0, 3]]
    
    for i, ans in enumerate(answers):
        if num_1[i % len(num_1)] == ans:
            students[0][0] += 1
        if num_2[i % len(num_2)] == ans:
            students[1][0] += 1
        if num_3[i % len(num_3)] == ans:
            students[2][0] += 1
        
    students.sort(key = lambda x: -x[0])
    answer = []
    for cnt, student in students:
        if students[0][0] <= cnt:
            answer.append(student)
        
    return sorted(answer)