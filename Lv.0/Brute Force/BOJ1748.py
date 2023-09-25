#1: 9, 2: 90 * 2 3: 900 * 3,..., R: 9 * 10 ** (R - 1) * R
#R: total(R-1) + R * (N - 10 ** (R-1) + 1)
N = int(input())
l = len(str(N))
ans = (N - 10 ** (l - 1) + 1) * l
for i in range(1, l):
    ans += (9 * 10 ** (i - 1)) * i
print(ans)