n, m = map(int,input().split())
arr = list(map(int,input().split()))
pos, neg = [], []
for i in range(n):
    if arr[i] > 0:
        pos.append(arr[i])
    else:
        neg.append(-arr[i])
pos.sort()
neg.sort()
all = [pos, neg]
total = 0

flag, cnt = 0, 0
max_value = 0
if len(pos) == 0:
    max_value = neg[-1]
    flag == 1
elif len(neg) == 0:
    max_value = pos[-1]
    flag == 0
else:
    max_value = max(pos[-1], neg[-1])
    if max_value == pos[-1]:
        flag = 0
    else:
        flag = 1
while True:
    if len(all[0]) < m and len(all[1]) < m:
        break
    elif len(all[flag]) < m:
        if flag == 1: flag = 0
        else: flag = 1
    if cnt == 0:
        total += all[flag][-1]
    else:
        total += 2 * all[flag][-1]
    for i in range(m):
        all[flag].pop()
    cnt += 1

if len(all[0]) == 0 and len(all[1]) == 0:
    total += 0
elif cnt == 0:
    if len(all[0]) == 0:
        total += all[1][-1]
    elif len(all[1]) == 0:
        total += all[0][-1]
    else:
        total += 2 * min(all[0][-1], all[1][-1]) + max(all[0][-1], all[1][-1])
else:
    if len(all[0]) == 0:
        total += 2 * all[1][-1]
    elif len(all[1]) == 0:
        total += 2 * all[0][-1]
    else:
        total += 2 * (all[0][-1] + all[1][-1])
print(total)