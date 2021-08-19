class User:

    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit (self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal (self, amount):
        self.account.withdraw(amount)  
        return self

    def display_user_balance (self):
        report = f"Usuario: {self.name}, Saldo: ${self.account.display_account_info()}"
        return report  
    
    def transfer_money (self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            self.balance -= 5
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bob = User("Bob Esponja","spongebob@squarepants.com")

guido.make_deposit(1000)
guido.make_withdrawal(300)
guido.transfer_money(monty, 200)
bob.make_withdrawal(100)
print(guido.display_user_balance())
print(monty.display_user_balance())
print(bob.display_user_balance())
