# Write your code here
from random import randint


class Customer:
    issuer_identification_number = 400000
    all_account_numbers = []

    def __init__(self):
        self.card_pin = randint(0000, 9999)
        # self.card_number_length = 16
        self.account_number = self.account_number_generator()
        self.checksum = randint(0, 9)
        self.card_number = self.card_number_generator()
        self.balance = 0

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
    customer_input = input("""1. Create an account
2. Log into account
0. Exit
""")

    cust1 = Customer()

    print(cust1.card_number)
    print(cust1.account_number)
    print(cust1.card_pin)


main()
