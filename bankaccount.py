class bankaccount():
    def __init__(self, account_holder, balance):
        self.balance = int(balance)
        self.account_holder = account_holder
    
    def deposit(self, deposit_amount):
            self.balance += deposit_amount
            print(f"You have deposited {self.deposit} Euros")
            print(f"Your new balance is {self.balance}")
    
    def withdraw(self, withdraw_amount):
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print(f"You have withdrawn {withdraw_amount}")
                print(f"Your new balance is {self.balance}")
                exit()
            else:
                print(f"You balance is {self.balance}; and it is insufficient")
    
    def display_amount(self):
         print(f"Your balance is {self.balance}")

transaction = bankaccount('maaz', '1000')
transaction.deposit(200)
transaction.withdraw(50)
transaction.display_amount()