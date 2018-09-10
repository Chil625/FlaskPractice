lottery_player_dict = {
    "name": "Rolf",
    "number": (5, 9, 12, 3, 1, 21)
}


class LotteryPlayer:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer("Rolf", (5, 9, 12, 3, 1, 21))
player_two = LotteryPlayer("John", (3, 7, 6, 91, 45))


# print(player_one.name)
# print(player_one.total())
# print(player_one == player_two)
# print(player_one.name == player_two.name)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        # print("I'm going to {}.".format(self.school))
        # print(self)
        print("I'm going to school.")


anna = Student("Anna", "MIT")
# anna.marks.append(56)
# anna.marks.append(71)
# print(anna.marks)
# print(anna.calculate_average())
anna.go_to_school()
Student.go_to_school()