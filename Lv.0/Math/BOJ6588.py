import sys

MAX = 1000001
cand = [True for i in range(MAX)]

for i in range(2, int(MAX ** 0.5) + 1):
    for j in range(2 * i, MAX, i):
        if cand[j]:
            cand[j] = False

while True:
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            break
    except:
        break
    s = 3
    while s <= n // 2:
        if cand[s] & cand[n - s]:
            sys.stdout.write("%d = %d + %d\n"%(n, s, n - s))
            break
        s += 2
    if s > n // 2:
        "Goldbach's conjecture is wrong."