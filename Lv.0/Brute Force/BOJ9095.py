import sys

def search(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return search(N - 1) + search(N - 2) + search(N - 3)

T = int(input())
for _ in range(T):
    n = int(input())
    sys.stdout.write(str(search(n)) + '\n')