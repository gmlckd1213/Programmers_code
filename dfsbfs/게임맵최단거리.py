from collections import deque
#임의의 그래프 그리는경우
def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    graph = [[-1 for _ in range(c)] for _ in range(r)]

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 1:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])

    answer = graph[-1][-1]
    return answer

#임의의 그래프 없이
from collections import deque
def solution(maps):
    answer = 0

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

                # 벽이면 무시하기
                if maps[nx][ny] == 0:  continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))    # 재귀

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[-1][-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer
