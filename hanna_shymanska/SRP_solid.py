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

class Order(Charge, Mailing, Sale):
    @staticmethod
    def final_order():
        print("It's your final order")
Charge.pay()
Mailing.send_mail()
Sale.generate_code()
Order.final_order()
Order.pay()
Order.send_mail()
Order.generate_code()