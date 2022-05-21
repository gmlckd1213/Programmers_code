#내풀이
def solution(s):
    answer=[]
    t=[]
    s1 = s[2:-2].split("},{")
    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    new_s.sort(key=len)  
    #sort 길이기준으로된다.
    for i in new_s:  
        int_list = list(map(int, i))
        answer.append(int_list)
    for i in answer:
        for j in range(len(i)):
            if i[j] not in t:
                t.append(i[j])
    return t
#다른사람풀이
def solution(s):
    answer=[]
    t=[]
    s1 = s[2:-2].split("},{")
    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    new_s.sort(key=len)  
    #sort 길이기준으로된다.
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


