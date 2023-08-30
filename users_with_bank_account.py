
class bankAccount:
    def __init__(self, int_rate =.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self


    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('Insufficient Funds')
        return self
        


    def display_account_info(self):
        print(f"Your Balance Is: ${self.balance}")
        return self


    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
    


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
    
    def create_account(self, account_name, int_rate=.02, balance=0):
        self.accounts[account_name] = bankAccount(int_rate, balance)
        return self
    
    def get_account(self, account_name):
        return self.accounts.get(account_name)
    
    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print('Account not found')
        return self

    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print('Account not found')
        return self
    
    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            print(f"User: {self.name}, Account: {account_name}, Balance: ${self.accounts[account_name].balance}")
        else:
            print(f"Account not found")
        return self
    
    
    def transfer_money(self, from_account, to_user, to_account, amount):
        if from_account in self.accounts and to_user in to_user.accounts:
            self.accounts[from_account].withdraw(amount)
            to_account.accounts[to_account].deposit(amount)  
        else:
            print("Accounts not found or invalid transfer")
        return self


# Test cases



Bryan = User("Bryan Walsh", 'email.com')
Bryan.create_account("Primary Account", int_rate=.05, balance=1000)
Bryan.create_account("Savings Account", int_rate=.06, balance=20000)

Bryan.make_deposit("Primary Account", 200).make_withdrawal("Primary Account", 500).display_user_balance('Primary Account')

Bryan.make_deposit("Savings Account", 200).make_withdrawal("Savings Account", 500).display_user_balance('Savings Account')


user2 = User('Jane Doe', 'anotheremail.com')
user2.create_account("Main Account", int_rate=.05, balance=1000000)

user2.make_deposit("Main Account", 10).display_user_balance("Main Account")

Bryan.transfer_money("Primary Account", user2, "Main Account", 2)
Bryan.display_user_balance("Primary Account")
user2.display_user_balance("Main Account")



