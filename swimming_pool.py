import sys
sys.stdin = open("swimming_pool_input.txt")

Test_Case = int(input())

for tc in range(Test_Case):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    day = price[0]
    month = price[1]
    three_month = price[2]
    year = price[3]

    print(price)
    print(plan)

    dp = [0] * 13

    count = 0
    for i in range(12):
        count += 1
        dp[i+1] = dp[i] + min(plan[i] * day, month)
        if count == 3:
            dp[i+1] = min(dp[i+1], three_month + dp[i-2])
            count -= 1

    if year < dp[12]:
        dp[12] = year
    print(dp)
    print(f'#{tc+1} {dp[12]}')