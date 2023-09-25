N = int(input())
price = [0]
price += list(map(int, input().split()))
DP = [0, price[1], ]
for i in range(2, N + 1):
    ans = 0
    for j in range(i):
        tmp = DP[j] + price[i - j]
        if ans < tmp:
            ans = tmp
    DP.append(ans)
print(DP[N])