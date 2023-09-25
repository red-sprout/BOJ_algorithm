#진행중
def calSn(n, y):
    s = 0
    while True:
        if (n * s) % y == 1: return s
        s += 1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    s1, s2 = calSn(N, M), calSn(M, N)
    print((x * s1 * M + y * s2 * N) % (M * N))