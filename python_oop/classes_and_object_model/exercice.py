#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
class Dog:
    def __init__(self, age):
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Insert money")
        after_deposit = self.balance + amount
        return after_deposit
    
    def withdraw(self, amount):
        if amount <= 0:
                raise ValueError("Select a valid amount")
        after_withdraw = self.balance - amount

        if after_withdraw < 0:
            print("Not enough funds")
        else:
            self.balance = after_withdraw
            return after_withdraw



if __name__ == "__main__":
    account = BankAccount(100)

    print(account.balance)

    account.deposit(50)

    print(account.balance)

    account.withdraw(30)

    print(account.balance)
