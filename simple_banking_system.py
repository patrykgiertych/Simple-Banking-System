import random

class CreditCard:
    def __init__(self, balance = 0):
        self.card_id = '400000'
        while len(self.card_id) < 16:
            self.card_id += str(random.randint(0,9))
        self.card_pin = ''
        while len(self.card_pin) < 4:
            self.card_pin += str(random.randint(0,9))
        self.balance = 0

    def card_id_pin(self, card):
        print(card.card_id)
        print(card.card_pin)

def loop_exit():
    print('Bye')
    exit()


while True:
    print('1. Create an account\n2. Log into account\n0. Exit')
    user = input()
    print()
    if user == '1':
        card_1 = CreditCard()
        print('Your card has been created')
        print(f'Your card number:\n{card_1.card_id}')
        print(f'Your card pin:\n{card_1.card_pin}')
        continue
    elif user == '2':
        logged_in = False
        while True:
            while not logged_in:
                print('Enter your card number:')
                card_number = input()
                print('Enter your PIN:')
                card_pin = input()
                if card_number == card_1.card_id and card_pin == card_1.card_pin:
                    print('You have successfully logged in!')
                    logged_in = True
                    break
                else:
                    print('Wrong card number or PIN!')
                    break
            print('\n1. Balance\n2. Log out\n0. Exit')
            user = input()
            print()
            if user == '1':
                print(f'Balance: {card_1.balance}')
                continue
            elif user == '2':
                print('You have successfully logged out!')
                break
            elif user == '0':
                loop_exit()
    elif user == '0':
        loop_exit()