from formulas import formula15


def exactness(x):
    if int(x) != x:
        buf = str(x).split('.')
        if len(buf[1]) >= 3:
            return False
    return True


k = 1
ak = formula15(k)/k
count = 1
while exactness(ak):
    k += 1
    ak = formula15(k)/k
    count += 1

print("ak =", ak)
print("Кількість ітерацій =", count)
