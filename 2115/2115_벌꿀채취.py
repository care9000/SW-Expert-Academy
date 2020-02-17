import sys
sys.stdin = open('2115_벌꿀채취.txt')


def collect_honey(i, j, M):
    global tem_result, tem_result_dubble
    honey_list = []
    for cnt in range(M):
        honey_list.append(mini_map[i][j + cnt])

    tem_result = 0
    tem_result_dubble = 0
    if sum(honey_list) > C:
        A = [0 for _ in range(M)]
        collect(A, 0, honey_list)
        return tem_result_dubble
    else:
        result = 0
        for honey in honey_list:
            result += honey ** 2
        return result


def collect(A, m, honey_list):
    global tem_result_dubble
    if m == M:
        tem_sum = 0
        tem_dubble = 0
        for k in range(M):
            if A[k]:
                tem_sum += honey_list[k]
                tem_dubble += honey_list[k] ** 2
        if tem_sum > C:
            return
        else:
            if tem_result_dubble < tem_dubble:
                tem_result_dubble = tem_dubble

    else:
        A[m] = 1
        collect(A, m + 1, honey_list)
        A[m] = 0
        collect(A, m + 1, honey_list)




T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, sys.stdin.readline().split())

    mini_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    tem_result = 0
    tem_result_dubble = 0
    result = 0
    for i in range(N):
        for j in range(N - (M - 1)):
            tem_result = 0
            person_1 = collect_honey(i, j, M)

            for k in range(i, N):
                if k == i:
                    for l in range(j + M, N - (M - 1)):
                        person_2 = collect_honey(k, l, M)
                        if person_1 + person_2 > result:
                            result = person_1 + person_2

                else:
                    for l in range(N - (M - 1)):
                        person_2 = collect_honey(k, l, M)
                        if person_1 + person_2 > result:
                            result = person_1 + person_2


    print("#{} {}".format(tc, result))
