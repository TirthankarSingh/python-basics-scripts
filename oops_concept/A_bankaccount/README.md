BankAccount Class — Assignment A1

A simple Python OOP implementation of a BankAccount to practice:

Class variables

Instance variables

__str__ method

Deposit & withdraw logic

Static method validation

🏦 Features

bank_name shared across all accounts

Validate numeric & positive amounts

Prevent withdrawal if balance is insufficient

Clean string representation using __str__

📌 Usage Example
from bank_account import BankAccount

# Create accounts
acc1 = BankAccount("Tirth", 50000000)
print(acc1)

# Deposit
acc1.deposit(6000)

# Withdraw
acc1.withdraw(2000000)

Example Output
Owner: Tirth, Balance: 50000000.0, BankName: SBI
Amount added to balance: 50006000.0 rs
Updated balance is: 48006000.0 rs

📂 File

assign_A1_bankaccount.py