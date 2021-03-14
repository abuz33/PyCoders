class BankAccount:

    '''Complete the methods below'''

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        self.fees = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.initial_balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal 
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
        return self.fees


########## Test your code by uncommenting the 4 lines below ########
'''  Test output should be that 10 and 5 are printed.  '''

# my_account = BankAccount(10)
# my_account.withdraw(15)
# my_account.deposit(20)
# print(my_account.get_balance(), my_account.get_fees())


######### Once your code passes the test, uncomment ########
######### the following 44 lines (all lines below)  ########
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print(my_account.get_balance(), my_account.get_fees())
