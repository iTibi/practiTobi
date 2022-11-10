from formulas import formula15
from math import factorial
from random import randint


def exactness(x):
    if int(x) != x:
        buf = str(x).split('.')
        if len(buf[1]) >= 3:
            return False
    return True


x = randint(1, 100)/100
k = 1
ak = (-1**k)*(formula15(k)*x**k)/factorial(k)
count = 1
while exactness(ak):
    k += 1
    ak = (-1**k)*(formula15(k)*x**k)/factorial(k)
    count += 1

print("ak =", ak)
print("Кількість ітерацій =", count)
