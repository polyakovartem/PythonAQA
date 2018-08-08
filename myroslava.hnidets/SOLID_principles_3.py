"""
This module related to homework with SOLID principles.
"""
__author__ = "Myroslava Hnidets"
__email__ = "Myroslava.Hnidets93@gmail.com"

import re


# The following InfoValidation class represents single responsibility principle

class InfoValidation(object):
    def mail_validation(self, mail):
        return re.match('[^@]+@[^@]+\.[^@]+', mail)

    def age_validation(self, age):
        return isinstance(age, int)

    def len_validation(self, name):
        return len(name) <= 15


# The following class ExpendedInfoValidation represents BAD example
# of Liskov substitution and Open/closed principles

# In this case we have a new class ExpendedInfoValidation, that inherits from InfoValidation class:
# mail_validation method from ExpendedInfoValidation class is overriding
# mail_validation method from InfoValidation class but not expends it.

class ExpendedInfoValidation(InfoValidation):
    def __init__(self):
        self.allowed_domains = ['.com', '.net', '.edu']

    def mail_validation(self, mail):
        pattern = re.search(r'[^@]+@[^@]+(\.[^@]+)', mail)
        if pattern:
            if pattern.group(1) in self.allowed_domains:
                return True


class AddUserInfo(InfoValidation):
    def __init__(self):
        super(AddUserInfo, self).__init__()
        self.user_id = 0
        self.user_info = {}

    def add_user_info(self, name, age, mail):
        self.user_id += 1

        if self.age_validation(age) and self.mail_validation(mail) and self.len_validation(name):
            self.user_info.update({
                self.user_id: {
                    'name': name,
                    'mail': mail,
                    'age': age
                }})

    def get_info(self):
        return self.user_info

    # The following method delete_first_user_info represents Interface Segregation Principle
    def delete_first_user_info(self):
        del self.user_info[1]
        return self.user_info


users = AddUserInfo()

users.add_user_info('Marko', 28, 'marko@gmail.com')
users.add_user_info('Mariaaaaaaaaaaaaaaaaaaaaaaaa', 21, 'maria@gmail.com')
users.add_user_info('Maria', '2', 'maria@gmail.com')
users.add_user_info('Maria', 21, '@gmail.com')

print(users.get_info())
# users.delete_first_user_info()
