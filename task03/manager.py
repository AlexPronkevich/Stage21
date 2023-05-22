# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 14.04.2023


from laptop import Laptop


class Manager:
    @staticmethod
    def summ_price(laptops):
        if isinstance(laptops, (list, tuple)):
            summ = 0
            for laptop in laptops:
                if isinstance(laptop, Laptop):
                    summ += laptop.price
            return summ

    @staticmethod
    def find_max_price(laptops):
        if isinstance(laptops, (list, tuple)):
            max_value = 300
            for laptop in laptops:
                if max_value < laptop.price:
                    max_value = laptop.price

            return max_value

    @staticmethod
    def find_min_price(laptops):
        if isinstance(laptops, (list, tuple)):
            min_value = 2000
            for laptop in laptops:
                if min_value > laptop.price:
                    min_value = laptop.price

            return min_value

