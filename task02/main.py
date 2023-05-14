# # Version 1.0
# # Author: Pronkevich Alexandra
# # Group: QA2022
# # Date: 09.04.2023


from human import Human
from manager import Manager
from human_creator import HumanCreator

ls = HumanCreator.create()

for human in ls:
    print(human)

adult = Manager.count_adult(ls)
underage = Manager.count_underage(ls)

print(f"Adult - {adult}")
print(f"Underage - {underage}")
