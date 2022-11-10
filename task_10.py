# 8.	Створити новий масив з негативних елементів масиву в.

from formulas import formula18


arr = []
for i in range(1, 8):
    y = formula18(i)
    arr.append(y)
print("Масив уk= F18(k): ", arr)

below_zero_arr = [x for x in arr if x < 0]
if len(below_zero_arr) == 0:
    print("Значення функції не має негативних значень")
else:
    print("Масив негативних значень у:", below_zero_arr)
