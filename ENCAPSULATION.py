class AccountError(Exception):{}
class BalanceError(Exception):{}

class BankAccount:
    def __init__(self, acct_num):
        self.__acct_num = acct_num
        self.__int_bal = 0

    @property
    def acct_num(self):
        return self.__acct_num

    @acct_num.setter
    def acct_num(self, new_acct_num):
        raise AccountError("Account number cannot be changed")

    @acct_num.deleter
    def acct_num(self):
        del self.int_bal
        self.__acct_num = None

    @property
    def int_bal(self):
        return self.__int_bal

    @int_bal.setter
    def int_bal(self,amount):
        if amount == 0:
            raise BalanceError("Cannot withdraw or deposite Zero amount")
        self.__int_bal = amount
        

    @int_bal.deleter
    def int_bal(self):
        if self.__int_bal < 0:
            raise BalanceError(f"Pending balances $ {self.__int_bal} /-")
        elif self.__int_bal > 0:
            print(f"Transfering $ {self.__int_bal} /-")
            self.__int_bal = 0



sourav = BankAccount(435679435)
print(f"Your account number is {sourav.acct_num}")
print(f"Your balance is $ {sourav.int_bal} /-")

try:
    del sourav.acct_num
except AccountError as e:
    print(f"Error: {e}")
except BalanceError as e:
    print(f"Error: {e}")

try:
    sourav.int_bal = 0
    print(f"Your balance is $ {sourav.int_bal} /-")
except AccountError as e:
    print(f"Error: {e}")
except BalanceError as e:
    print(f"Error: {e}")

try:
    sourav.int_bal = 100
    print(f"Your balance is $ {sourav.int_bal} /-")
except AccountError as e:
    print(f"Error: {e}")
except BalanceError as e:
    print(f"Error: {e}")

try:
    del sourav.acct_num
    print(f"Your balance is $ {sourav.int_bal} /-")
except AccountError as e:
    print(f"Error: {e}")
except BalanceError as e:
    print(f"Error: {e}")

try:
    del sourav.int_bal
    print(f"Your balance is $ {sourav.int_bal} /-")
except AccountError as e:
    print(f"Error: {e}")
except BalanceError as e:
    print(f"Error: {e}")

try:
    del sourav.acct_num
    print(f"Your balance is $ {sourav.int_bal} /-")
except AccountError as e:
    print(f"Error: {e}")
except BalanceError as e:
    print(f"Error: {e}")

