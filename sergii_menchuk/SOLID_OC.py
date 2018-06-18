from abc import ABCMeta


class Personal(object):
    __metaclass__ = ABCMeta

    def salary_increase(self):
        pass


class Teacher(Personal):

    def __init__(self, salary, increase_percentage):
        self.salary = salary
        self.increase_percentage = increase_percentage

    def salary_increase(self):
        return self.salary * self.increase_percentage


class SalaryIncreaseCalculator:
    def __init__(self, personal):
        self.personal = personal

    def total_increase(self):
        total = 0
        for personal in self.personal:
            total += personal.salary_increase()
        return total


def main():
    personal = [Teacher(1000, 0.02), Teacher(1500, 0.01)]
    total_increase = SalaryIncreaseCalculator(personal)

    print("The total salary increase of all personal is: ${}".format(total_increase.total_increase()))


if __name__ == '__main__':
    main()
