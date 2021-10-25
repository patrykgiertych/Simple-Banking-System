# Simple-Banking-System

## Description

First Python project for learning object-oriented programming and SQL. 
This app allows user to create a bank account. After creating the account, user will receive his credit card number and PIN. Credit card numbers are generated using Luhn algorithm, which is used for validating credit cards. PIN is a 4-digit random number. 
After logging in using these credentials, user can check his balance, add money to his account, transfer money to other accounts or delete his account.

## How to run

To run the program, download the simple_banking_system.py file and run it as python script.

## How to use

After running the program this is what we get in the terminal:

```
1. Create an account
2. Log into account
0. Exit
```

To perform an action, input the corresponding number into the console and press enter.

## Example

```
1. Create an account
2. Log into account
0. Exit

>1
Your card has been created
Your card number:
4000008982088820
Your card pin:
6608
1. Create an account
2. Log into account
0. Exit

>2
Enter your card number:
4000008982088820
Enter your PIN:
6608
You have successfully logged in!


1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit

1
Balance: 0      

1. Balance      
2. Add income   
3. Do transfer  
4. Close account
5. Log out      
0. Exit

2
Enter income:
10000
Income was added!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit

5
You have successfully logged out!
1. Create an account
2. Log into account
0. Exit
```


