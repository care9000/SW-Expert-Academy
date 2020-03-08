import sys
sys.stdin = open('1247_최적_경로.txt')

def Pem(n, m, distance):
    global min_distance
    if min_distance <= distance:
        return

    if n == m:
        tem = abs(info[-4] - info[-2]) + abs(info[-3] - info[-1])
        if distance + tem < min_distance:
            min_distance = distance + tem
            return

    else:
        for k in range(m, n, 2):
            info[m], info[m + 1], info[k], info[k + 1] = info[k], info[k + 1], info[m], info[m + 1]
            tem = abs(info[m - 2] - info[m]) + abs(info[m - 1] - info[m + 1])
            Pem(n, m + 2, distance + tem)
            info[m], info[m + 1], info[k], info[k + 1] = info[k], info[k + 1], info[m], info[m + 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    info = list(map(int, input().split()))
    info.append(info.pop(2))
    info.append(info.pop(2))
    min_distance = 987654321
    Pem((N * 2) + 2, 2, 0)
    print("#{} {}" .format(tc, min_distance))
