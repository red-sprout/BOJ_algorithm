import sys

def gcd(A, B):
    R = A%B
    while R:
        A = B
        B = R
        R = A % B
    return B


input = lambda : sys.stdin.readline().rstrip()

N = int(input())
tree = [0] * N
cnt = 0

for i in range(N):
    tree[i] = int(input())

start = tree[0]
end = tree[N-1] + 1

B = tree[1] - tree[0]
for i in range(1, N-1):
    A = tree[i+1] - tree[i]
    B = gcd(A, B)
    if B == 1: break

idx = 0
for i in range(start, end, B):
    if i == tree[idx]:
        idx += 1
        continue
    cnt += 1

print(cnt)