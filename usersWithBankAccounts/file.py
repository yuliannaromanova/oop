class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else: 
            print("your balance isnt enought : Charngin a 5$ fee" )
            self.balance -= 5
    def display_account_info(self):
        print("Balance : {}".format(self.balance))
        return self.balance
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self



    @classmethod
    def get_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name ):
        self.name = name
        self.account = {
            "checking": BankAccount (0.02, 500),
            "savings": BankAccount (0.05, 1000)
        }
    def display_user_balance (self):
        print ("user:" + self.name + "checking balance:" + str(self.account['checking'].display_account_info())) 
        print ("user:" + self.name + "savings balance:" + str(self.account['savings'].display_account_info())) 
        return self
    def transfer_money (self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance ()
        user.display_user_balance ()
        return self
Luiza = User ("Luiza")
Luiza.account['checking'].deposit (100)
Luiza.display_user_balance()