# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 09.04.2023


import random
import string
from human import Human


class HumanCreator:
    @staticmethod
    def create(size=5):
        humans = []
        FIRSTNAMES = ("Anna", "Alice", "Vladimir",
                      "Nataly", "Alex", "Maks", "Ivan")
        SURNAMES = ("Ivanov", "Miller", "Rivs", "Collins",
                    "Glushko", "Kruger", "Martinez")
        MAX_AGE = 100
        MIN_AGE = 1

        for _ in range(size):
            human = Human()
            human.firstname = random.choice(FIRSTNAMES)
            human.surname = random.choice(SURNAMES)
            human.age = random.randint(MIN_AGE, MAX_AGE)
            human.is_alive = random.choice((True, False))
            humans.append(human)

        return humans
