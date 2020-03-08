import sys
sys.stdin = open('1865_동철이의_일분배.txt')


def Pem(N, m, info):
    global max_percentage
    if max_percentage >= info:
        return
    if N == m:
        if max_percentage < info:
            max_percentage = info
            return

    else:
        for k in range(m, N):
            order[m], order[k] = order[k], order[m]
            Pem(N, m + 1, (info * data[m][order[m]]) / 100)
            order[m], order[k] = order[k], order[m]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    order = [i for i in range(N)]
    max_percentage = 0
    Pem(N, 0, 1)
    max_percentage = round(max_percentage * 100, 6)
    max_percentage = format(max_percentage, '.6f')
    print("#{} {}" .format(tc, max_percentage))