from itertools import permutations

def solution(numbers):
    answer = []
    a=[]
    for i in permutations(numbers):
        result = ''.join(map(str, i))
        a.append(int(result))
    
    return str(sorted(a, reverse=True)[0])


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))