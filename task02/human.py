# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 09.04.2023

class Human:
    def __init__(self, firstname='no name', surname='no name', age=0, alive=True):
        self.__firstname = firstname
        self.__surname = surname
        self.__age = age
        self.__alive = alive

    @property
    def firstname(self):
        return self.__firstname.capitalize()

    @firstname.setter
    def firstname(self, firstname):
        if isinstance(firstname, str):
            self.__firstname = firstname

    @property
    def surname(self):
        return self.__surname.capitalize()

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age=1):
        if 0 < age <= 120:
            self.__age = age

    @property
    def is_alive(self):
        return "Yes" if self.__alive else "No"

    @is_alive.setter
    def is_alive(self, alive):
        if isinstance(alive, bool):
            self.__alive = alive

    def __str__(self):
        return f"{self.__firstname} {self.__surname} : age = {self.__age}. " \
               f"Is alive? - {self.is_alive}."
