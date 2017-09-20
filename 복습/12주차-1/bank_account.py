class BankAccount:
    def __init__(self, customer_name, balance=0):
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다.")
        else:
            self.balance = self.balance - amount

        return self.balance

    def show_account(self):
        print("Customer Name : "+ str(self.customer_name))
        print("Balance : "+ str(self.balance))
            
