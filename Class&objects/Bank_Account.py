class Account:
    # Initializing an account with the set parameters
    def __init__(self, full_name, acc_num, phone_no, balance): # method/ function constructor --> set up info
        #init -- initialize/add
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone_no = phone_no
        self.balance = balance

    # Depositing
    def deposit(self, amount):
        self.balance = self.balance + amount # when depositing in a bank it's adding the deposited amount to the account balance
        print(f"Dear {self.full_name}, Amount ${amount} has been deposited successfully to account {self.acc_num}. New balance  is ${self.balance}") # Another way of printing by using format

    # Withdrawing
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Dear {self.full_name}, Your balance has Insufficient Funds. Balance is ${self.balance}. To access loans, press 1 to continue.")

        else:
            self.balance = self.balance - amount
            print(f"Dear {self.full_name}, Amount ${amount} has been withdrawn from account ${self.acc_num}. Remaining balance is ${self.balance}.")

    # Check balance
    def check_balance(self):
        print(f"Dear {self.full_name}, your balance for account ${self.acc_num} is: {self.balance}")

# Adding Accounts
larry_acc = Account("Larry Guru", 10046710, "0758781717", 10000000)
mary_acc = Account("Mary Kamau", 29771530, "079825415", 20000)
fred_acc = Account("Fredrick Mwangumu", 64777330, "0756243592", 90000)


# Depositing, Withdrawing, Checking Balance
# Larry's Transactions
# Larry's Transactions
larry_acc.deposit(200000)
larry_acc.withdraw(500)
larry_acc.check_balance()

# Mary's Transactions
mary_acc.deposit(20)
mary_acc.withdraw(100000000)
mary_acc.check_balance()

# Fred's Transactions
fred_acc.deposit(200000)
fred_acc.withdraw(500)
fred_acc.check_balance()


