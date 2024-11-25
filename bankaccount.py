class bankaccount():
    def __init__(self, account_holder, balance):
        self.balance = int(balance)
        self.account_holder = account_holder
        self.transactions = []
    
    def deposit(self, deposit_amount):
            self.balance += deposit_amount
            print(f"You have deposited {deposit_amount}$")
            print(f"Your new balance is {self.balance}$")
            self.transactions.append (f"Deposited {deposit_amount}$")
    
    def withdraw(self, withdraw_amount):
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print(f"You have withdrawn {withdraw_amount}$")
                print(f"Your new balance is {self.balance}$")
                self.transactions.append (f"Withdrawn {withdraw_amount}$")
                exit()
            else:
                print(f"You balance is {self.balance}$; and it is insufficient")
    
    def display_amount(self):
        print(f"Account name with name {self.account_holder} has balance of {self.balance}$")
    
    def statement(self):
        print("Your statements are below:\n")
        print(self.transactions)         

account1 = bankaccount('maaz', '1000')
account1.deposit(200)
account1.withdraw(50)
account1.display_amount()
account1.statement()

account2 = bankaccount('omar', '2000')
account2.deposit(200)
account2.withdraw(50)
account2.display_amount()
account2.statement()