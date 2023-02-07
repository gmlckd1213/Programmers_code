from collections import defaultdict

def solution(tickets):
    dic = defaultdict(list)

    for start, end in tickets:
        dic[start].append(end)  # key = 출발, value = 도착

    def dfs():
        stack = ["ICN"]
        while stack:
            airport = stack[-1]
            if airport not in dic or not dic[airport] :
                visited.append(stack.pop())
            else :
                stack.append(dic[airport].pop(0))

    visited = []
    for k in dic.keys() :
        dic[k].sort() # 값들 오름차순 정렬
    dfs()

    return visited[::-1]