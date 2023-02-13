def solution(array, commands):
    answer = []
    for c in commands:
        arr = array[c[0]-1:c[1]]
        arr.sort()
        t=arr[c[2]-1]
        answer.append(t)
        
    return answer





