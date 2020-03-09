import sys
sys.stdin = open('7699_수지의_수지_맞는_여행.txt')

import collections

def bfs():
    q = collections.deque([])
    q.append([0, 0, mini_map[0][0]])
    tem_result = 0
    while len(q):
        i, j, info = q.popleft()

        if len(info) > tem_result:
            tem_result = len(info)
            if tem_result == 26:
                break

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if ispass(nx, ny) and mini_map[nx][ny] not in info:
                q.append([nx, ny, info + mini_map[nx][ny]])

    return tem_result


def ispass(i, j):
    if -1 < i < R and -1 < j < C:
        return True

    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    mini_map = [input() for _ in range(R)]
    print("#{} {}" .format(tc, bfs()))
