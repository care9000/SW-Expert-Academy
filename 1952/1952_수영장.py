import sys
sys.stdin = open('1952_수영장.txt')


def dfs(month, price):
    global min_price
    if min_price < price:
        return

    elif month > 11:
        min_price = price

    else:
        if month_list[month]:
            dfs(month + 1, price + (month_list[month] * price_list[0]))
            dfs(month + 1, price + price_list[1])
            dfs(month + 3, price + price_list[2])

        else:
            dfs(month + 1, price)


T = int(input())
for tc in range(1, T + 1):
    price_list = list(map(int, input().split()))
    month_list = list(map(int, input().split()))

    min_price = 987654321
    dfs(0, 0)
    if min_price > price_list[3]:
        min_price = price_list[3]

    print("#{} {}" .format(tc, min_price))