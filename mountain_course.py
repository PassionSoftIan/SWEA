import sys
sys.stdin = open("mountain_course_input.txt")

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def find_route(stack, drill, height, count):
    global max_result

    while stack:
        n, m = stack.pop()
        for k in range(4):
            ny, nx = n + dy[k], m + dx[k]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                if arr[ny][nx] < height:
                    visited[ny][nx] = 1
                    find_route([[ny, nx]], drill, arr[ny][nx], count + 1)
                    visited[ny][nx] = 0

                else:
                    for p in range(1, K + 1):
                        if arr[ny][nx] - p < height and drill == 0:
                            visited[ny][nx] = 1
                            find_route([[ny, nx]], drill + 1, arr[ny][nx] - p, count + 1)
                            visited[ny][nx] = 0

                    else:
                        if max_result < count:
                            max_result = count


Test_Case = int(input())

for tc in range(Test_Case):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    check = []

    max_height = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_height:
                max_height = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_height:
                check.append([i, j])

    max_result = 0

    for stk in check:
        visited[stk[0]][stk[1]] = 1
        find_route([stk], 0, arr[stk[0]][stk[1]], 1)
        visited[stk[0]][stk[1]] = 0

    print(f'#{tc + 1} {max_result}')