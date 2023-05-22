# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 08.05.2023


class Zebra():
    def __init__(self, name="no name"):
        self.__name = name
        self.__state = True

    def get_stripe(self):
        msg = "black line" if self.__state else "white line"
        msg += f" from zebra {self.__name}  "
        self.__state = not self.__state

        return msg
