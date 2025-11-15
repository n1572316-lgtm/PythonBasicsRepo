def get_total(products_dict):

    products_dict (dict):
    float/int:

    total_amount = 0
    for price in products_dict.values():
        total_amount += price
    return total_amount

 products = {
     "хлеб": 60,
     "молоко": 80,
     "сыр": 150
 }

total_sum = get_total(products)
total_items = len(products)

print(f"Всего товаров: {total_items}")
print(f"Общая сумма" {total_sum} руб.")