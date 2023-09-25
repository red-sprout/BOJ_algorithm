MAX = 10 ** 6

N = int(input())
# cand = [MAX, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
cand = [MAX, 0]
for i in range(2, N + 1):
    cand.append(min(cand[i - 1], cand[i // 2 if not i % 2 else 0], cand[i // 3 if not i % 3 else 0]) + 1)
print(cand[N])