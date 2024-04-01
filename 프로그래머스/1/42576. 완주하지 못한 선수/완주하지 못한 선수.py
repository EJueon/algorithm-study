def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if len(completion) <= i:
            return participant[i]
        elif participant[i] != completion[i]:
            return participant[i]
    