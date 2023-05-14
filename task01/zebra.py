# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 08.04.2023

class Zebra:
    def __init__(self, line="black line", i=0):
        self.line = line
        self.i = i

    def get_stripe():
        self.i = 0
        for self.i in range(10):
            if self.i % 2 == 0:
                self.line = "black line"
                return f"{self.line} ."
            else:
                self.line = "white line"
                return f"{self.line} ."
        self.i += 1

    def __str__(self):
        return f"{self.line} ."
