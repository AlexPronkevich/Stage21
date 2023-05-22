# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 14.04.2023


from laptop import Laptop
from manager import Manager
from laptop_creator import LaptopCreator

ls = LaptopCreator.create()

for laptop in ls:
    print(laptop)

summ = Manager.summ_price(ls)
max_value = Manager.find_max_price(ls)
min_value = Manager.find_min_price(ls)

# print(result)
print(f"Общая стоимость ноутбуков - {summ}")
print(f"Цена самого дорогого ноутбука - {max_value}")
print(f"Цена самого дешевого ноутбука - {min_value}")

