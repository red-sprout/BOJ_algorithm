CONST = 1000000009
MAX = 100000

T = int(input())
end1, end2, end3 = [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1]

for i in range(4, MAX + 1):
    end1.append((end2[i-1] + end3[i-1]) % CONST)
    end2.append((end1[i-2] + end3[i-2]) % CONST)
    end3.append((end1[i-3] + end2[i-3]) % CONST)

for _ in range(T):
    N = int(input())
    print((end1[N] + end2[N] + end3[N]) % CONST)