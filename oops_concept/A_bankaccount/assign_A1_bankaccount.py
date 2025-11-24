class BankAccount:
    bank_name = "SBI"

    def __init__(self, owner, balance=0):
        self.owner = owner
        try:
            self.balance = float(balance)
        except (TypeError, ValueError):
            print("Initial balance must be a number.")
        if self.balance < 0:
            print("Initial balance cannot be negative.")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}, BankName: {BankAccount.bank_name}"

    def deposit(self, amount):

        try:
            if float(amount) > 0:
                self.balance = self.balance + float(amount)
                print("Amount added to balance: {} rs".format(self.balance))
            elif float(amount) < 0:
                print("Invalid Amount deposited")

        except ValueError:
            print("Invalid amount deposit. check the amount again")

    def withdraw(self, amount):
        status = BankAccount.validate_amount(self.balance, float(amount))

        if status == "Valid":
            self.balance = self.balance - float(amount)
            print("Updated balance is: {} rs".format(self.balance))

        else:
            print("Insufficient balance")

    @staticmethod
    def validate_amount(balance, amount):
        return "Valid" if balance - amount >= 0 else "invalid"


BA = BankAccount("Tirth", 50000000)
print(BA)
BA.deposit(6000)
BA.withdraw(2345322)

BA = BankAccount("irthhhh", 500000)
print(BA)
BA.deposit("abxd")
BA.withdraw(2345322)
