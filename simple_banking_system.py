import random

class CreditCard:
    card_id = None
    card_pin = None
    balance = 0

    def create_id():
        CreditCard.card_id = '400000'
        while len(CreditCard.card_id) < 15:
            CreditCard.card_id += str(random.randint(0,9))
        count = 1
        multiplied = []
        minus= []
        for i in CreditCard.card_id:
            if count % 2 != 0:
                i = int(i) * 2
                multiplied.append(i)
            else:
                multiplied.append(i)
            count += 1
        for i in multiplied:
            if int(i) > 9:
                i = int(i) - 9
                minus.append(i)
            else:
                minus.append(i)
        digits_sum = sum([int(i) for i in minus])
        if digits_sum % 10 == 0:
            CreditCard.card_id += '0'
        else:
            rem = digits_sum % 10
            checksum = 10 - rem
            CreditCard.card_id += str(checksum)

    def create_pin():
        CreditCard.card_pin = ''
        while len(CreditCard.card_pin) < 4:
            CreditCard.card_pin += str(random.randint(0,9))
    
    def create_credit_card():
        CreditCard.create_id()
        CreditCard.create_pin()
        print('Your card has been created')
        print(f'Your card number:\n{CreditCard.card_id}')
        print(f'Your card pin:\n{CreditCard.card_pin}')
        CreditCard.main_menu()

    def main_menu():
        print('1. Create an account\n2. Log into account\n0. Exit\n')
        user = input()   
        if user == '1':
            CreditCard.create_credit_card()
        elif user == '2':
            CreditCard.login()
        elif user == '0':
            CreditCard.exit()
    
    def login():
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        card_pin = input()
        if card_number == CreditCard.card_id and card_pin == CreditCard.card_pin:
            print('You have successfully logged in!\n')
            CreditCard.logged_in()
        else:
            print('Wrong card number or PIN!')
            CreditCard.main_menu()

    def logged_in():
        print('\n1. Balance\n2. Log out\n0. Exit\n')
        user = input()
        if user == '1':
            print(f'Balance: {CreditCard.balance}')
            CreditCard.logged_in()
        elif user == '2':
            print('You have successfully logged out!')
            CreditCard.main_menu()
        elif user == '0':
            CreditCard.exit()

    def exit():
        print('Bye')
        quit()

CreditCard.main_menu()