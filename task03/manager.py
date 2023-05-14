# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 14.04.2023


from laptop import Laptop


class Manager:

    def summ_price(laptops):
        if isinstance(laptops, (list, tuple)):
            return Laptop()

        summ = 0
        for laptop in laptops:
            if isinstance(laptop, Laptop):
                summ += laptop.__price
        return summ

    def find_max_price(laptops):
        max_value = laptop.__price[0]

        for laptop.__price in laptops:
            if max_value < laptop.__price:
                max_value = laptop.__price

        return max_value

    def find_min_price(laptops):
        min_value = laptop.__price[0]

        for laptop.__price in laptops:
            if min_value < laptop.__price:
                min_value = laptop.__price

        return min_value
