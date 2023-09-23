MAX = 1000001

N = int(input())
M = int(input())
malf = list(map(int, input().split()))

m = abs(N - 100)
ans = m

for i in range(MAX):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in malf:
            break
        elif j == len(num) - 1:
            ans = min(ans, len(num) + abs(N - i))

print(ans)