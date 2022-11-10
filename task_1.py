# 8.   Ціни на два види товарів зросли на р відсотків. Вивести старі і нові ціни.

product1 = 400
product2 = 1300

p = 20

new_product1 = product1 + product1/100*p
new_product2 = product2 + product2/100*p

print("Old price: ", product1)
print("New price: ", new_product1)
print("Old price: ", product2)
print("New price: ", new_product2)
