N = int(input())
I = input()
G = input()
TF = [I[i] == G[i] for i in range(N)]

ans = 0

for i in range(1, N-1):
    if TF[i - 1]:
        continue
    TF[i] = not TF[i]
    TF[i + 1] = not TF[i + 1]
    TF[i - 1] = not TF[i - 1]
    ans += 1
    print(TF)

# if False in TF:
#     print(-1)
# else:
#     print(ans)