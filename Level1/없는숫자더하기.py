def solution(numbers):
    arr = [0,1,2,3,4,5,6,7,8,9]
    no = []
    for i in arr:
        if i not in numbers:
            no.append(i)
    answer=sum(no)
        
    return answer