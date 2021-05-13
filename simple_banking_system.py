import random
import sqlite3


class CreditCard:
    def __init__(self, number = None, pin = None, balance = 0 ):
        self.number = self.create_number
        self.pin = self.create_pin
        self.balance = balance
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.create_db()

    def create_db(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS card (id integer not null primary key, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
        self.conn.commit()
        

    def card_insert(self, num, pin_):
        self.cur.execute(f'insert into card (number, pin) values ({num}, {pin_})')
        self.conn.commit()
        

    def db_check(self, num, pin):
        self.cur.execute(f"select number, pin from card where number={num}")
        self.cred = self.cur.fetchone()
        self.conn.commit()
        if pin == self.cred[1]:
            return True
        else:
            return False
        

    def create_number(self):
        self.number = '400000'
        while len(self.number) < 15:
            self.number += str(random.randint(0,9))
        count = 1
        minus= []
        count = 1
        for i in self.number:
            if count % 2 != 0:
                i = int(i) * 2
                if int(i) > 9:
                    i = int(i) - 9
                minus.append(i)
            else:
                minus.append(i)
            count += 1
        digits_sum = sum([int(i) for i in minus])
        if digits_sum % 10 == 0:
            self.number += '0'
        else:
            rem = digits_sum % 10
            checksum = 10 - rem
            self.number += str(checksum)
        return self.number
    
    def create_pin(self):
        self.pin = ''
        while len(self.pin) < 4:
            self.pin += str(random.randint(0,9))
        return self.pin
        
    def create_credit_card(self):
        number = self.create_number()
        pin = self.create_pin()
        self.card_insert(number, pin)
        print('Your card has been created')
        print(f'Your card number:\n{number}')
        print(f'Your card pin:\n{pin}')
        self.main_menu()

    def main_menu(self):
        print('1. Create an account\n2. Log into account\n0. Exit\n')
        user = input()   
        if user == '1':
            self.create_credit_card()
        elif user == '2':
            self.login()
        elif user == '0':
            self.exit()
    
    def login(self):
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        card_pin = input()
        if self.db_check(card_number,card_pin):
            print('You have successfully logged in!\n')
            self.logged_in()
        else:
            print('Wrong card number or PIN!')
            self.main_menu()

    def logged_in(self):
        print('\n1. Balance\n2. Log out\n0. Exit\n')
        user = input()
        if user == '1':
            print(f'Balance: {self.balance}')
            self.logged_in()
        elif user == '2':
            print('You have successfully logged out!')
            self.main_menu()
        elif user == '0':
            self.exit()

    def exit(self):
        print('Bye')
        self.conn.close()
        quit()

ATM = CreditCard()
ATM.main_menu()
