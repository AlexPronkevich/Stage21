# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 19.05.2023

from zebra import Zebra
import random


def main():
    zebra1 = Zebra("Milly")
    zebra2 = Zebra("Gaspar")
    zebra3 = Zebra("Princess")

    zebras = (zebra1, zebra2, zebra3)

    for _ in range(10):
        zebra = random.choice(zebras)
        print(zebra.get_stripe())


if __name__ == "__main__":
    main()
