#진행중
def calSn(n, y):
    s = 0
    while True:
        if (n * s) % y == 1: return s
        s += 1

year = list(map(int, input().split()))
E, S, M = 15, 28, 19
m = E * S * M
n1, n2, n3 = S * M, E * M, E * S
s1, s2, s3 = calSn(n1, E), calSn(n2, S), calSn(n3, M)

print((year[0] * n1 * s1 + year[1] * n2 * s2 + year[2] * n3 * n3) % m)