import sys
sys.stdin = open('1861_정사각형_방.txt')


def simulation():
    # 큰 값부터 하나씩 꺼내서 표시
    max_dp, max_num = 0, N ** 2
    while len(data):
        num, i, j = data.pop()
        dp[i][j] = 1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and room[nx][ny] - 1 == room[i][j]:
                dp[i][j] += dp[nx][ny]
                if check(max_dp, max_num, dp[i][j], num):
                    max_dp = dp[i][j]
                    max_num = num
                break

    return max_num, max_dp


# 그 방의 정보가 가장 많은 방을 이동 가능하고 적힌 방의 숫자가 낮을 경우
def check(max_dp, max_num, tem_dp, num):
    if tem_dp > max_dp:
        return True

    elif tem_dp == max_dp and num < max_num:
        return True

    return False


# 이동 가능 한 방이 있는지 확인
def ispass(i, j):
    if -1 < i < N and -1 < j < N:
        return True

    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]
    data = []
    for i in range(N):
        for j in range(N):
            data.append([room[i][j], i, j])
    data = sorted(data)
    result_num, result_max = simulation()
    print("#{} {} {}" .format(tc, result_num, result_max))
