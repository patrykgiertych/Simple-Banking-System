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
 
    # create a db method
    def create_db(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS card (id integer not null primary key, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
        self.conn.commit()
 
    # insert credit card info into db
    def card_insert(self, num, pin_):
        self.cur.execute(f'insert into card (number, pin) values ({num}, {pin_})')
        self.conn.commit()
 
    # check credentials 
    def db_check(self, num, pin):
        self.cur.execute(f"select number, pin from card where number={num}")
        self.cred = self.cur.fetchone()
        self.conn.commit()
        if pin == self.cred[1]:
            return True
        else:
            return False
  
    # generate credit card number with luhn algorithm 
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
    
    # generate credit card pin
    def create_pin(self):
        self.pin = ''
        while len(self.pin) < 4:
            self.pin += str(random.randint(0,9))
        return self.pin

    # merged create_number, create_pin, card_insert  
    def create_credit_card(self):
        number = self.create_number()
        pin = self.create_pin()
        self.card_insert(number, pin)
        print('Your card has been created')
        print(f'Your card number:\n{number}')
        print(f'Your card pin:\n{pin}')
        self.main_menu()

    # main menu
    def main_menu(self):
        print('1. Create an account\n2. Log into account\n0. Exit\n')
        user = input()   
        if user == '1':
            self.create_credit_card()
        elif user == '2':
            self.login()
        elif user == '0':
            self.exit()
    
    # nav method
    def login(self):
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        card_pin = input()
        if self.db_check(card_number,card_pin):
            print('You have successfully logged in!\n')
            self.logged_in(card_number)
        else:
            print('Wrong card number or PIN!')
            self.main_menu()
    
    # nav method
    def logged_in(self, number):
        self.cur.execute(f'select number, pin, balance from card where number={number}')
        self.conn.commit()
        info = self.cur.fetchone()
        print('\n1. Balance\n2. Add income\n3. Log out\n0. Exit\n')
        user = input()
        if user == '1':
            print(f'Balance: {info[2]}')
            self.logged_in(number)
        elif user == '2':
            self.add_income(number)
        elif user == '3':
            print('You have successfully logged out!')
            self.main_menu()
        elif user == '0':
            self.exit()
    
    # nav method
    def exit(self):
        print('Bye')
        self.conn.close()
        quit()

    # add income method
    def add_income(self, number):
        print('Enter income:')
        income = int(input())
        print('Income was added!')
        self.cur.execute(f'update card set balance=balance+{income} where number={number}')
        self.conn.commit()
        self.logged_in(number)
        


ATM = CreditCard()
ATM.main_menu()
