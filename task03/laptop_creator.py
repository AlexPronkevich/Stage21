# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 13.04.2023


import random
import string
from laptop import Laptop


class LaptopCreator:
    @staticmethod
    def create(size=5):
        laptops = []
        BRAND = ("Sony", "Apple", "HP", "ASUS", "Acer")
        MODEL = ("SV-E1512W1R/B", "A2485", "255 G9 6S6F2EA", "F515EA-BQ1993W",
                    "515-57-59F2 NH.QESEP.OOC")
        MAX_PRICE = 2000
        MIN_PRICE = 300

        for _ in range(size):
            laptop = Laptop()
            laptop.brand = random.choice(BRAND)
            laptop.model = random.choice(MODEL)
            laptop.price = random.randint(MIN_PRICE, MAX_PRICE)
            laptops.append(laptop)

        return laptops
