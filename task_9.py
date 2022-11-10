# 8.    Обчислити суму всіх збитків. У якому році фірма мала найбільшої збиток? Яка його величина?

from formulas import formula17
from prettytable import PrettyTable

arr = []
table = PrettyTable()
table.field_names = ['рік', 'величина доходу']
for x in range(1991, 2002):
    y = round(100 * formula17(x), 2)
    arr.append(y)
    table.add_row([x, y])
print(table)

loss_arr = [x for x in arr if x < 0]

print("Сума збитків =", round(sum(loss_arr), 2))
print("Найбільший збиток =", min(loss_arr),
      "у", 1991+arr.index(min(arr)), "році")
