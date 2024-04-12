income = int(input())
s = income
k = 0
while income != 0:
    income = int(input())
    s += income
    k += 1
print(s / k)
