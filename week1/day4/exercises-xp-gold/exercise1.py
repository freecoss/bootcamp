class BankAccount():
    # part 1
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, add):
        if int(add)>=0:
            self.balance+=add
        else:
            raise ValueError("the deposit number should be positive!")
        
    def withdraw(self, minus):
        if int(minus)>=0:
            self.balance-=minus
        else:
            raise ValueError("the deposit number should be positive!")
        
# part 2
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance=0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance
        
    def withdraw(self, minus):
        if (self.balance-int(minus))>self.minimum_balance:
            if int(minus)>=0:
                self.balance-=minus
            else:
                raise ValueError("the deposit number should be positive!")
        else:
            raise ValueError("the balance can't be lower than the minimum balance!")
