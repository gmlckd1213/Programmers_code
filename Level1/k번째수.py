def solution(array, commands):
    q = []
    answer = []
    for t in commands:
        
        
        answer = array[t[0]-1:t[1]]
        answer.sort()
        p=answer[t[2]-1]
        q.append(p)
        
    return q

