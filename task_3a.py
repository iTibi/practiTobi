from math import tan, log, exp
from formulas import formula10, formula11


def fi(x, a, b):
    return round(tan(x+a)-log(abs(b+7), 8), 3)


def omega(x, c, d):
    return round(c*(x**2+d*exp(1.3))**0.2, 3)


# Скласти дві програми, використовуючи:
# а) повну форму команди розгалуження if;

x = int(input("x << "))

if abs(x) < 10:
    print(formula10(fi(x, int(input("a << ")), int(input("b << ")))))
else:
    print(formula11(omega(x, int(input("c << ")), int(input("d << ")))))


# б) коротку форму команди розгалуження if.

print(formula10(fi(x, int(input("a << ")), int(input("b << "))))) if abs(
    x) < 10 else print(formula11(omega(x, int(input("c << ")), int(input("d << ")))))
