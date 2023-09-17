MAX = 1000001
arr = [0 for i in range(MAX+1)]
for i in range(1, MAX+1):
    j = 1
    while i * j <= MAX:
        arr[i * j] += i
        j += 1
for i in range(1, MAX+1):
    arr[i] = arr[i-1] + arr[i]

T = int(input())
ans = []
for i in range(T):
    S = int(input())
    ans.append(str(arr[S])+'\n')
print(''.join(ans))

# BOJ17427.py
# N = int(input())
# ans = 0
# for i in range(1, N+1):
#     ans += i * (N // i)
# print(ans)