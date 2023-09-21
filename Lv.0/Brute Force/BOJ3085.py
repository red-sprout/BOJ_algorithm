#진행중
import sys

arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    arr.append(list(input()))

check = []
dummy = 1

for i in range(N):
    for j in range(N - 1):
        temp = arr[i][j]
        arr[i][j] = arr[i][j + 1]
        arr[i][j + 1] = temp

        for l in range(N):
            for m in range(N - 1):
                if arr[l][m] == arr[l][m + 1]:
                    dummy += 1
            check.append(dummy)

        dummy = 1

        for l in range(N):
            for m in range(N - 1):
                if arr[m][l] == arr[m + 1][l]:
                    dummy += 1
            check.append(dummy)
        
        dummy = 1

        temp = arr[i][j]
        arr[i][j] = arr[i][j + 1]
        arr[i][j + 1] = temp

for i in range(N):
    for j in range(N - 1):
        temp = arr[j][i]
        arr[j][i] = arr[j + 1][i]
        arr[j + 1][i] = temp

        for l in range(N):
            for m in range(N - 1):
                if arr[l][m] == arr[l][m + 1]:
                    dummy += 1
            check.append(dummy)

        dummy = 1

        for l in range(N):
            for m in range(N - 1):
                if arr[m][l] == arr[m + 1][l]:
                    dummy += 1
            check.append(dummy)
        
        dummy = 1

        temp = arr[j][i]
        arr[j][i] = arr[j + 1][i]
        arr[j + 1][i] = temp

print(max(check))