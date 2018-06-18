"""
This module describes a homework related to SOLID.
Dependency inversion principle
"""
__author__ = "Iryna Pavlyk"
__email__ = "iruska.m1@ukr.net"

from abc import abstractmethod


class ISalary(object):

    @abstractmethod
    def calculate_salary(self):
        pass


class ManagerSalary(ISalary):

    def __init__(self, salary, premium, tax):
        self.salary = salary
        self.tax = tax
        self.premium = premium

    def calculate_salary(self):
        return self.salary * self.premium * (1 - self.tax / 100)


class InternSalary(ISalary):

    def __init__(self, salary, premium, tax):
        self.salary = salary
        self.tax = tax
        self.premium = premium

    def calculate_salary(self):
        return self.salary * self.premium * (1 - self.tax / 100)


class WorkerSalary(ISalary):

    def __init__(self, salary, premium, tax):
        self.salary = salary
        self.tax = tax
        self.premium = premium

    def calculate_salary(self):
        return self.salary * self.premium * (1 - self.tax / 100)


if __name__ == '__main__':
    manager = ManagerSalary(1000, 2.5, 30)
    print(manager.calculate_salary())
    worker = WorkerSalary(700, 1.25, 25)
    print(worker.calculate_salary())
    intern = InternSalary(500, 1, 15)
    print(intern.calculate_salary())
