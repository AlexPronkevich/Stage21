# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 13.04.2023


class Laptop:
    def __init__(self, brand='no name', model='no name', price=0):
        self.__brand = brand
        self.__model = model
        self.__price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self.__model = model

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price=0):
        self.__price = price

    def __str__(self):
        return f"Laptop: {self.__brand}, model = {self.__model}, price = ${self.__price}, "
