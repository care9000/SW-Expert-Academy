import sys
sys.stdin = open('2382_미생물_격리.txt')
import collections


def simulation():
    for microbe in microbe_location:
        # 미생물이 있으면
        if microbe[2]:
            move(microbe[0], microbe[1], microbe[2], microbe[3])

    for i in range(N):
        for j in range(N):
            if len(mini_map[i][j]) > 1:
                combine(i, j)


# 한 공간에 2개이상의 미생물이 있을 경우 에는 결합
def combine(i, j):
    max_num = 0
    max_cnt = 0
    tem_sum = 0
    for k in range(len(mini_map[i][j])):
        if mini_map[i][j][k][0] > max_cnt:
            max_cnt = mini_map[i][j][k][0]
            max_num = mini_map[i][j][k][1]
            
        tem_sum += mini_map[i][j][k][0]
        
    for k in range(len(mini_map[i][j])):
        if max_num != mini_map[i][j][k][1]:
            microbe_location[mini_map[i][j][k][1]][2] = 0
            
    microbe_location[max_num][2] = tem_sum
    mini_map[i][j] = collections.deque([])
    mini_map[i][j].append([tem_sum, max_num])


# 미생물을 이동시키는 함수
def move(i, j, cnt, k):
    global total_cnt
    tem = mini_map[i][j].popleft()
    num = tem[1]
    i_tem = i + dx[k]
    j_tem = j + dy[k]
    # 벽을 만났을 경우 회전 시켜야됨
    if ischeck(i_tem, j_tem):
        total_cnt -= cnt
        cnt //= 2
        total_cnt += cnt
        if k % 2:
            k += 1

        else:
            k -= 1

    microbe_location[num][0], microbe_location[num][1], microbe_location[num][2], microbe_location[num][3] = i_tem, j_tem, cnt, k
    mini_map[i_tem][j_tem].append([cnt, num])


def ischeck(i, j):
    if i == 0 or i == N - 1 or j == 0 or j == N - 1:
        return True

    return False


dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    microbe_location = [list(map(int, input().split())) for _ in range(K)]
    mini_map = [[collections.deque([]) for _ in range(N)] for _ in range(N)]
    dummy = 0
    total_cnt = 0
    for microbe in microbe_location:
        mini_map[microbe[0]][microbe[1]].append([microbe[2], dummy])
        total_cnt += microbe[2]
        dummy += 1

    time = 0
    while time < M:
        simulation()
        time += 1

    print("#{} {}" .format(tc, total_cnt))


