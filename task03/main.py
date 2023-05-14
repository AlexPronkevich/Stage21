# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 14.04.2023


from laptop import Laptop
from manager import Manager


def main():
    laptop1 = Laptop("Sony", "SV-E1512W1R/B", 620)
    laptop2 = Laptop("Apple", "A2485", 1050)
    laptop3 = Laptop("HP", "255 G9 6S6F2EA", 690)
    laptop4 = Laptop("ASUS", "F515EA-BQ1993W", 480)
    laptop5 = Laptop("Acer", "515-57-59F2 NH.QESEP.OOC", 1200)

    laptops = (laptop1, laptop2, laptop3, laptop4, laptop5)

    summ = Manager.summ_price(laptops)
    max_value = Manager.find_max_price(laptops)
    min_value = Manager.find_min_price(laptops)

    # print(result)
    print(f"Общая стоимость ноутбуков - {summ}")
    print(f"Цена самого дорогого ноутбука - {max_value}")
    print(f"Цена самого дешевого ноутбука - {min_value}")


if __name__ == "__main__":
    main()
