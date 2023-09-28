CONST = 1000000000

arr = [[0, 0]]
arr += [[0, 1] for _ in range(9)]

N = int(input())

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            arr[j].append((arr[j + 1][i - 1]) % CONST)
        elif j == 9:
            arr[j].append((arr[j - 1][i - 1]) % CONST)
        else:
            arr[j].append((arr[j + 1][i - 1] + arr[j - 1][i - 1]))

ans = 0
for i in range(10):
    ans += arr[i][N]

print(ans % CONST)