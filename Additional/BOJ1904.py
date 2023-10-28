n = int(input())
before, after = 1,2
ans = before
for i in range(1, n+1):
    if i == 1:
        continue
    else:
        tmp = before
        before = after
        after += tmp
        ans = before
        continue
print(ans)