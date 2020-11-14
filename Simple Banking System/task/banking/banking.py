# Write your code here
from random import randint


class Customer:
    issuer_identification_number = 400000
    customer_details = {}
    number_of_customers = 0
    all_account_numbers = []

    def __init__(self):
        self.card_pin = randint(1000, 9999)
        # self.card_number_length = 16
        self.account_number = self.account_number_generator()
        self.checksum = randint(0, 9)
        self.card_number = self.card_number_generator()
        self.balance = 0
        self.account_details = [self.card_number, self.card_pin, self.balance]
        self.number_of_customers += 1

        self.customer_details = {self.number_of_customers: self.account_details}

    def account_number_generator(self):
        new_acc_num = randint(000000000, 999999999)
        for acc_num in self.all_account_numbers:
            if new_acc_num == acc_num:
                new_acc_num = randint(000000000, 999999999)

        self.all_account_numbers.append(new_acc_num)
        return new_acc_num

    def card_number_generator(self):
        string_card_number = str(self.issuer_identification_number) + \
                             str(self.account_number) + str(self.checksum)

        return int(string_card_number)


# TODO
# There should be a bank class which should have all the account numbers,
# card numbers and card pins etc created in that session.
# Then there should be a create account class which should be a subclass of
# bank class.
# and then another class for logging in, which also should be a subclass of
# bank class.


def main():
    i = 0
    while i < 2:
        customer_input = int(input("""1. Create an account
2. Log into account
0. Exit
"""))
        print()
        customer = Customer()
        if customer_input == 0:
            print('Bye!')
            return
        elif customer_input == 1:
            print('Your card number:')
            print(customer.card_number)
            print('Your card PIN:')
            print(customer.card_pin)
            print()
        else:
            input_card_number = int(input("""Enter your card number:
"""))
            input_card_pin = int(input("""Enter your PIN:
"""))
            for k, v in customer.customer_details.items():
                if v[0] == input_card_number and v[1] == input_card_pin:
                    print('You have successfully logged in!')

                    customer_input = int(input("""1. Balance
2. Log out
0. Exit
"""))
                    print()
                    if customer_input == 0:
                        print("""Bye!""")
                        return
                    elif customer_input == 1:
                        print('Balance: ', v[2])
                        return
                    else:
                        print('You have successfully logged out!')
                        return

                else:
                    print('Wrong card number or PIN!')
                    print()


main()
