MAX = 1000000
CONST = 1000000009
DP = [0, 1, 2, 4]
for i in range(4, MAX + 1):
    DP.append((DP[i - 1] + DP[i - 2] + DP[i - 3]) % CONST)

T = int(input())
for _ in range(T):
    n = int(input())
    print(DP[n])