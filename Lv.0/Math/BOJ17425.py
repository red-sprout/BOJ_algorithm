MAX = 1000000
T = int(input())
for i in range(T):
    g = 0
    N = int(input())
    for i in range(1, N + 1):
        g += i * (N // i)
    print(g)