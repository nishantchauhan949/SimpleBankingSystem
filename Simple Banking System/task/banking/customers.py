from random import randint
import sqlite3


class Customer:
    issuer_identification_number = 400000
    customer_details = {}
    number_of_customers = 0
    all_account_numbers = []

    def __init__(self):
        self.card_pin = randint(1000, 9999)
        self.account_number = self.account_number_generator()
        self.checksum = 0
        self.card_number = self.card_number_generator()
        self.balance = 0
        self.account_details = [self.card_number, self.card_pin, self.balance]
        Customer.number_of_customers += 1

        Customer.customer_details[self.number_of_customers] = self.account_details

    def account_number_generator(self):
        new_acc_num = randint(100000000, 999999999)
        for acc_num in Customer.all_account_numbers:
            if new_acc_num == acc_num:
                new_acc_num = randint(100000000, 999999999)

        Customer.all_account_numbers.append(new_acc_num)
        return new_acc_num

    def card_number_generator(self):
        return self.luhn_implementation()

    def luhn_implementation(self):
        # card number without checksum
        string_card_number = str(self.issuer_identification_number) + \
                          str(self.account_number)

        list_card_number = []

        for number in string_card_number:
            list_card_number.append(int(number))

        card_number_by_2 = list_card_number.copy()

        for index in range(0, len(card_number_by_2), 2):
            card_number_by_2[index] *= 2

        for index in range(0, len(card_number_by_2)):
            if card_number_by_2[index] > 9:
                card_number_by_2[index] -= 9

        add_all_numbers = 0
        for num in card_number_by_2:
            add_all_numbers += num

        if add_all_numbers % 10 != 0:
            self.checksum = 10 - (add_all_numbers % 10)

        list_card_number.append(self.checksum)

        some_string = ''
        for num in list_card_number:
            some_string += str(num)

        final_card_number = int(some_string)
        return final_card_number

