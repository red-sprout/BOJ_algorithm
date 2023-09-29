end_0 = [0,0,1]
end_1 = [0,1,0]
N = int(input())
for i in range(3, N + 1):
    end_1.append(end_0[i - 1])
    end_0.append(end_0[i - 1] + end_1[i - 1])
print(end_0[N] + end_1[N])