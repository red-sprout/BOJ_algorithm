import sys

arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    arr.append(list(input()))

check = []
check_part = []
dummy = 1

for i in range(N):
    for j in range(N - 1):
        arr[i][j], arr[i][j + 1] = arr[i][j+1], arr[i][j]

        for l in range(N):
            for m in range(N - 1):
                if arr[l][m] == arr[l][m + 1]:
                    dummy += 1
                else:
                    dummy = 1
                check.append(dummy)
            check_part = []
            dummy = 1

        for l in range(N):
            for m in range(N - 1):
                if arr[m][l] == arr[m + 1][l]:
                    dummy += 1
                else:
                    dummy = 1
                check.append(dummy)
            check_part = []
            dummy = 1

        arr[i][j], arr[i][j + 1] = arr[i][j+1], arr[i][j]

for i in range(N):
    for j in range(N - 1):
        arr[j][i] , arr[j + 1][i] = arr[j + 1][i] , arr[j][i]

        for l in range(N):
            for m in range(N - 1):
                if arr[l][m] == arr[l][m + 1]:
                    dummy += 1
                else:
                    dummy = 1
                check_part.append(dummy)
            check.append(max(check_part))
            check_part = []
            dummy = 1

        for l in range(N):
            for m in range(N - 1):
                if arr[m][l] == arr[m + 1][l]:
                    dummy += 1
                else:
                    dummy = 1
                check_part.append(dummy)
            check.append(max(check_part))
            check_part = []
            dummy = 1

        arr[j][i] , arr[j + 1][i] = arr[j + 1][i] , arr[j][i]

print(max(check))