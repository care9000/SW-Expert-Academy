import sys
sys.stdin = open('2814_최장_경로.txt')

def dfs(i, tem):
    global tem_distance
    if tem > tem_distance:
        tem_distance = tem

    for j in range(N):
        if node[i][j] and vertex[j] == 0:
            vertex[j] = 1
            dfs(j, tem + 1)
            vertex[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    dummys = [list(map(int, input().split())) for _ in range(M)]
    node = [[0 for _ in range(N)] for _ in range(N)]
    # 노드에 표시
    for dummy in dummys:
        node[dummy[0] - 1][dummy[1] - 1] = 1
        node[dummy[1] - 1][dummy[0] - 1] = 1

    distance = 1
    for i in range(N):
        # 노드에 표시
        vertex = [0 for _ in range(N)]
        tem_distance = 0
        vertex[i] = 1
        dfs(i, 1)
        if tem_distance > distance:
            distance = tem_distance
            # 이이상은 나올 수 없음.
            if distance == N:
                break
    print("#{} {}" .format(tc, distance))