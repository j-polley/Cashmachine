class BankAccount:
    def __init__(self, account_holder, account_type='current', pin=None):
        self.account_holder = account_holder
        self.balance = 0
        self.transaction_history = []
        self.account_type = account_type
        self.pin = pin  # PIN for authentication (optional for now)
        self.max_withdrawal = 1000 if account_type == 'current' else 500  # Example limit for savings accounts

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        self.transaction_history.append(f"Deposited: £{amount}")
        return f"£{amount} deposited successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient balance."
        if amount > self.max_withdrawal:
            return f"Exceeded withdrawal limit of £{self.max_withdrawal} for {self.account_type} account."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: £{amount}")
        return f"£{amount} withdrawn successfully."

    def view_transaction_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        return "\n".join(self.transaction_history)

    def authenticate(self, pin):
        if self.pin is None:  # No PIN set, authentication is not required
            return True
        return self.pin == pin


def main():
    print("Welcome to James Cash Machine Simulation!")
    account_holder = input("Enter account holder's name: ")

    # Account setup: ask for account type and PIN
    account_type = input("Enter account type (currnt/savings): ").lower()
    if account_type not in ['current', 'savings']:
        print("Invalid account type. Defaulting to 'current'.")
        account_type = 'current'

    pin = input("Set a 4-digit PIN (or press Enter to skip): ")
    pin = pin if pin else None
    if pin and len(pin) != 4:
        print("Invalid PIN. PIN must be 4 digits. Proceeding without PIN.")
        pin = None

    account = BankAccount(account_holder, account_type, pin)

    # Authentication loop
    authenticated = False
    while not authenticated:
        entered_pin = input("Enter your 4-digit PIN to authenticate (or press Enter to skip): ")
        if account.authenticate(entered_pin):
            authenticated = True
            print("Authentication successful!")
        else:
            print("Invalid PIN. Please try again.")

    # Main menu loop
    while True:
        print("\nPlease select an option:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View transaction history")
        print("5. Exit")

        try:
            choice = int(input("Enter choice (1-5): "))

            if choice == 1:
                print(f"Current balance: £{account.check_balance()}")
            elif choice == 2:
                amount = float(input("Enter amount to deposit: £"))
                print(account.deposit(amount))
            elif choice == 3:
                amount = float(input("Enter amount to withdraw: £"))
                print(account.withdraw(amount))
            elif choice == 4:
                print("\nTransaction History:")
                print(account.view_transaction_history())
            elif choice == 5:
                print("Thank you for using James Cash Machine. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        time.sleep(1)  # Adding a small delay before showing the menu again


if __name__ == "__main__":
    main()
