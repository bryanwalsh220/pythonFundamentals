
class bankAccount:
    def __init__(self, int_rate =.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Thank you for depositing ${amount} your new balance is ${self.balance}")


    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'you have withdrawn ${amount}, your new balance is ${self.balance}')
        else:
            self.balance -= 5
            print(f'we are sorry, you have insufficient funds and have been chaged a $5 fee')
        


    def display_account_info(self):
        print(f"Your Balance Is: ${self.balance}")


    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f"Interest has been applied to your account, your new balance is ${self.balance}")

account1 = bankAccount()
account2 = bankAccount(.04, 1000)

# account1.display_account_info()
# account1.deposit(50)
# account1.withdraw(100)
# account1.display_account_info()
# account1.deposit(100)
# account1.withdraw(50)
# account1.display_account_info()
# account1.yield_interest()


account2.display_account_info()
account2.deposit(50)
account2.withdraw(1000)
account2.display_account_info()
account2.deposit(100000)
account2.withdraw(500080)
account2.display_account_info()
account2.yield_interest()


