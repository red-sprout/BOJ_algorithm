# BOJ 1793 타일링
MAX = 251
arr = [1, 1, 3]
for i in range(3, MAX):
    arr.append(arr[i - 1] + 2 * arr[i - 2])
while True:
    try:
        n = int(input())
        print(arr[n])
    except:
        break