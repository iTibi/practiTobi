# 8.1 стопка = 0.0568 л = 0.00012 пайпа;

from prettytable import PrettyTable


table = PrettyTable()
table.field_names = ["Стопка", "л", "пайп"]

strings = int(input("Amount strings << "))
step = int(input("Step << "))

for i in range(1, strings*step, step):
    table.add_row([i, round(i*0.0568, 5), round(i*0.00012, 5)])
print(table)
