a, b = map(int, input().split())
ans = 0
m = min(a, b) + 1
for i in range(1, m):
    if (a % i) + (b % i) == 0:
        ans = i
print(ans)
print(ans * (a // ans) * (b // ans))