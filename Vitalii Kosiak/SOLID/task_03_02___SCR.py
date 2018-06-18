"""
This module describes a homework related to homework SOLID SRP.
"""
import random
import datetime as dt

class Order:
    """This class contains tools for order."""
    def __init__(self, customer, email, cart, date):
        self.customer = customer
        self.cart = list(cart)
        self.email = email
        self.date = date

    def charge(self):
        """This method get paynement from customer."""
        print('Get paynement from %s' % self.customer.upper())
        # get money from customer
        
    def show_details(self):
        """This method show details."""
        print('Name = {} \nEmail = {} \nCart = {} \nDate = {}'.format(self.customer, self.email, self.cart, self.date))


class Mailer(Order):
    
    def send_mail(self, content):
        cont = content
        print('Emailing... to {}, on {}, text is "{}"'.format(self.customer, self.email, cont))
        # send `content` to mail `customer`


class Coupon:
    def __init__(self, code=None):
        code = code if code is not None else Coupon.generate_code()
    def generate_code():
        print('code = ' + str(random.randint(10001, 99999)))
        # generate code of cupone


zakaz1 = Order('customer_name', 'viths@i.ua', ['pos1','pos2','pos3'], str(dt.datetime.now()))
zakaz1.charge()
zakaz1.show_details()
mail1 = Mailer.send_mail(zakaz1, 'Contet of email')
coupon1 = Coupon.generate_code()
