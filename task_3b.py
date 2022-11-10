from formulas import formula10, formula11, formula12

work_types = {"А": 0.1, "Б": 0.15, "В": 0.2}
while True:
    work_type = input("Work type << ")
    if work_type in work_types:
        break

if work_type == "А":
    all_money = 100*abs(formula10(8)+50)
elif work_type == "Б":
    all_money = 150*abs(formula11(8)+100)
elif work_type == "В":
    all_money = 200*abs(formula12(8)+135)

tax = all_money * work_types[work_type]
money_to_receive = all_money-tax

print("Вся сума = ", round(all_money, 3))
print("Податок = ", round(tax, 3))
print("До видачі =", round(money_to_receive, 3))
