class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        self.fees = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.initial_balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal
        resulting in a negative balance also deducts a penalty 
        fee of 5 dollars from the balance.
        """
        if self.initial_balance - amount < 0:
            self.initial_balance = self.initial_balance - amount - 5
            self.fees += 5
        else:
            self.initial_balance -= amount

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees


########## Test your code by uncommenting the 4 lines below ########
'''  Test output should be that 10, 5, 5, and 0 are printed.  '''
account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)
print(account1.get_balance(), account1.get_fees(),
      account2.get_balance(), account2.get_fees())


########## Once your code passes the test, uncomment ########
########## the following 55 lines (all lines below)  ########

account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)
print(account1.get_balance(), account1.get_fees(),
      account2.get_balance(), account2.get_fees())
