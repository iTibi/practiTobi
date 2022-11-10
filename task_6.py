from formulas import formula13, formula14


x = 0
k = 1
while k <= 13:
    x += formula13(k)
    k += 1
y = 1
k = 1
while k <= 13:
    y *= formula14(k)
    k += 1

z = round(x**2+3*y, 3)
print("z =", z)
