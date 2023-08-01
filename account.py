class Account:
    def __init__(self, number, user, balance, limite):
        print(f'Building account ... {self}')
        self.__number = number
        self.__user = user
        self.__balance = balance
        self.__limite = limite

    def statement(self):
        print(f'Your balance is {self.__balance} from account {self.__user}')

    def deposit(self, amount):
        self.__balance += amount

    def __user_withdraw(self, amount_withdraw):
        available_withdraw = self.__balance + self.__limite
        return available_withdraw >= amount_withdraw  # Corrected the comparison operator to check if enough balance available.

    def withdraw(self, amount):
        if self.__user_withdraw(amount):
            self.__balance -= amount
        else:
            print(f'The amount {amount} is insufficient for your limit.')

    def transfer(self, amount, sender):
        self.withdraw(amount)
        sender.deposit(amount)

    @property
    def balance(self):
        return self.__balance

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def branch_code():
        return "001"

    @staticmethod
    def branches_code():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


account1 = Account(123, 'Julio', 234.50, 10000)
account2 = Account(456, 'Andre', 344.50, 12000)
account3 = Account(789, 'Joe', 94.50, 10300)



# Instances to be used

print(account1.balance) 
print(account2.balance)
print(account3.balance)


# To make a deposit 

account1.deposit(100)
print(account1.balance)

account2.withdraw(50)
print(account2.balance)

# To transfer between accounts 

account1.transfer(50, account3)
print(account1.balance)
print(account3.balance)


