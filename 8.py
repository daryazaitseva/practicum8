for i in range(1, 10):
    s = '123456789'
    n = int(s[:i])
    res = n * 8 + i
    print(f"{n} * 8 + = {res}")

for i in range(1, 10):
    s = '123456789'
    n = int(s[:i])
    res = n * 9 + (i + 1)
    print(f"{n} * 9 + {i + 1} = {res}")

for i in range(1, 10):
    s = '111111111'
    n = int(s[:i])
    res = n * n
    print(f"{n} * {n} = {res}")
