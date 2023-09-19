N = int(input())
cand = list(map(int, input().split()))
count = N
for i in cand:
    if i == 1:
        count -= 1
        continue
    for j in range(2, i):
        if (i % j) == 0:
            count -= 1
            break
print(count)