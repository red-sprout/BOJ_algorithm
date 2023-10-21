N = int(input())
A = list(map(int,input().split()))
left, right, result = [1] * N, [1] * N, [0] * N

for i in range(1, N):
        for j in range(0, i):
            if A[i] > A[j]:
                left[i] = max(left[i], left[j] + 1)

for i in range(N - 2, -1, -1):
        for j in range(N - 1, i, -1):
            if A[i] > A[j]:
                right[i] = max(right[i], right[j] + 1)

for i in range(N):
     result[i] = left[i] + right[i] - 1

print(max(result))