class Charge:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = list(cart)
    @staticmethod
    def pay():
        print('Payment for all products')


class Mailing:
    @staticmethod
    def send_mail():
        print('This is an email about order')


class Sale:
    @staticmethod
    def generate_code():
        print('Generating code for each customer')


Charge.pay()
Mailing.send_mail()
Sale.generate_code()