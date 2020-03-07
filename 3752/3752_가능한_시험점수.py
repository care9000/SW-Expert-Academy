import sys
sys.stdin = open('3752_가능한_시험점수.txt')

def simulation():
    cnt = 1
    for score in score_info:
        # 뒤에서 부터 해줌 (앞에서 부터 하면 계속 커지기 떄문에)
        for i in range(9901, -1, -1):
            if dp[i] == 1 and dp[i + score] == 0:
                dp[i + score] = 1
                cnt += 1

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    score_info = list(map(int, input().split()))
    dp = [0 for _ in range(10001)]
    dp[0] = 1
    print("#{} {}".format(tc, simulation()))
