# 8.   Обчислити кількість негативних і кількість позитивних значень функції y.
from formulas import formula16
from prettytable import PrettyTable


table = PrettyTable()
table.field_names = ['x', 'y']

i = 0
arr = []
while i <= 8:
    y = formula16(i)
    arr.append(y)
    table.add_row([round(i, 1), y])
    i = i+0.8


print(table)

nums_below_zero = [y for y in arr if y < 0]
nums_under_zero = [y for y in arr if y > 0]

print("Кількість негативних значень y =", len(nums_below_zero))
print("Кількість позитивних значень y =", len(nums_under_zero))
