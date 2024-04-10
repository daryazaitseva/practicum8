a = int(input())
maximum = -1
k = 0
while a != -1:
    a = int(input())
    k += 1
    if a > maximum:
        maximum = a
print(k)
