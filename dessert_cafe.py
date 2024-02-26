import sys
sys.stdin = open("dessert_cafe_input.txt")

dy = [1, 1, -1, -1, 0]
dx = [1, -1, -1, 1, 0]


def find_route(depth, n, m):
    global max_result

    if depth == 2:
        if max_result > len(result) * 2:
            return

    if depth == 3 and n == i and m == j:
        max_result = max(max_result, len(result))
        return

    for k in range(depth, depth + 2):
        ny, nx = n + dy[k], m + dx[k]
        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] not in result:
            result.append(arr[ny][nx])
            find_route(k, ny, nx)
            result.pop()


Test_Case = int(input())

for tc in range(Test_Case):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_result = -1

    for i in range(N):
        for j in range(N):
            result = []
            find_route(0, i, j)

    print(f'#{tc+1} {max_result}')