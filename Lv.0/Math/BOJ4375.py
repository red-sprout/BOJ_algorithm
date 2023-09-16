while True:
    try:
        n = int(input())
    except:
        break
    value, i = '1', 1
    while True:
        if int(value) % n == 0: break
        i += 1
        value += '1'
    print(i)