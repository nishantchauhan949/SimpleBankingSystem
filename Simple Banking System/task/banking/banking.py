from customers import Customer


def main():
    i = 0
    while i < 2:
        customer_input = int(input("""1. Create an account
2. Log into account
0. Exit
"""))
        print()

        if customer_input == 0:
            print('Bye!')
            return
        elif customer_input == 1:
            customer = Customer()
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
            for k, v in Customer.customer_details.items():
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


if __name__ == '__main__':
    main()