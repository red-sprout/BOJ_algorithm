import sys

cand = []
for _ in range(9):
    cand.append(int(sys.stdin.readline()))

total = sum(cand)
index = []

for i in range(9):
    for j in range(i + 1, 9):
        if total - cand[i] - cand[j] == 100:
            index = [i, j]
            break

cand = cand[:index[0]] + cand[index[0] + 1:index[1]] + cand[index[1] + 1:]
cand.sort()

for i in range(7):
    sys.stdout.write(str(cand[i]) + '\n')