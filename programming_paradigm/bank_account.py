class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        print(f"[DEBUG] Account created with balance: {self.account_balance}")

    def deposit(self, amount):
        print(f"[DEBUG] deposit() called with amount: {amount}")
        print(f"[DEBUG] Balance BEFORE deposit: {self.account_balance}")
        if amount > 0:
            self.account_balance += amount
            print(f"[DEBUG] Balance AFTER deposit: {self.account_balance}")
            return True
        else:
            print("Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        print(f"[DEBUG] withdraw() called with amount: {amount}")
        print(f"[DEBUG] Balance BEFORE withdraw: {self.account_balance}")

        if amount < self.account_balance:
            self.account_balance -= amount
            print(f"[DEBUG] Balance AFTER withdraw: {self.account_balance}")

        else:
            print("Insufficient funds or invalid amount.")
            return False
        return True

    def display_balance(self):
        print(f"[DEBUG] display_balance() called")
        print(f"Current Balance: ${self.account_balance}")
