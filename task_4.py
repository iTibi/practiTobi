# 8.    Ввести номер місяця. Вивести назву часу року.

while True:
    month = int(input("Month's number << "))
    if 1 <= month <= 12:
        break


if 1 <= month <= 2 or month == 12:
    print("Winter")
elif 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
else:
    pass


if 1 <= month <= 2 or month == 12:
    print("Winter")
if 3 <= month <= 5:
    print("Spring")
if 6 <= month <= 8:
    print("Summer")
if 9 <= month <= 11:
    print("Autumn")
