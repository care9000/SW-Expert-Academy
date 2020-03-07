import sys
sys.stdin = open('2819_격자판의_숫자_이어_붙이기.txt')

def dfs(i, j, info):
    # 길이가 7개가 되면 담고 리턴을 해줘야 함
    if len(info) == 7:
        result.append(info)
        return

    # 방문에 그 정보가 담겨져 있지 않으면 담고 담겨 있으면 굳이 할 필요가 없다.
    if info not in vis:
        vis[i][j].append(info)
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny):
                dfs(nx, ny, info + str(data[nx][ny]))

    else:
        return


def ispass(i, j):
    if -1 < i < 4 and -1 < j < 4:
        return True

    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    data = [list(map(int, input().split())) for _ in range(4)]
    vis = [[[] for _ in range(4)] for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, str(data[i][j]))

    result = list(set(result))
    print("#{} {}" .format(tc, len(result)))
