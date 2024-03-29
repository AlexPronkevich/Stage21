# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 09.04.2023


from human import Human


class Manager:
    @staticmethod
    def count_adult(humans):
        if isinstance(humans, (list, tuple)):
            count = 0
            for human in humans:
                if isinstance(human, Human) and human.age >= 18:
                    count += 1
            return count

    @staticmethod
    def count_underage(humans):
        total = len(humans)
        total -= Manager.count_adult(humans)
        return total
