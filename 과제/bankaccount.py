# 장민수
# 컴퓨터 공학과
# 201331040

class BankAccount:

    def __init__(self, customer_name, balance=0):
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, money):
        self.balance = self.balance + money
        return self.balance

    def withdraw(self, money):
        if self.balance<money:
            print("잔액이 부족합니다.")
        else:
            self.balance = self.balance - money

        return self.balance

    def show_account(self):
        print("Customer Name :",self.customer_name)
        print("Bakabce : ", self.balance)


    
