#BOJ1188
#유클리드 호제법으로 최대공약수
N, M = map(int,input().split())
a, gcd = max(N, M), min(N, M)
while True:
    if a % gcd != 0:
        tmp = gcd
        gcd = a % gcd
        a = tmp
    else:
        break
print(M - gcd)