#exercise bank account
#1
class BankAccount:
    def __init__(self, balance=0, username="", password=""):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Deposit amount must be a positive integer")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive integer")
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance -= amount
        return self.balance

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, username="", password="", minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdrawal amount must be a positive integer")
        if (self.balance - amount) < self.minimum_balance:
            raise Exception("Withdrawal exceeds minimum balance limit")
        self.balance -= amount
        return self.balance

#part 4 Create an atm class
class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list) or not all(isinstance(acc, BankAccount) for acc in account_list):
            raise Exception("Invalid account list")
        
        try:
            if not isinstance(try_limit, int) or try_limit <= 0:
                raise Exception("Invalid try limit")
        except Exception:
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

    def log_in(self, username, password):
        matched_account = None
        for acc in self.account_list:
            if acc.authenticate(username, password):
                matched_account = acc
                break

        if matched_account:
            self.current_tries = 0
            self.show_account_menu(matched_account)
        else:
            self.current_tries += 1
            print(f"Invalid credentials. Try {self.current_tries} of {self.try_limit}")
            if self.current_tries >= self.try_limit:
                print("Reached max tries. Shutting down the program.")
                exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu ({account.username}) ---")
            print(f"Current Balance: {account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit to Main Menu")
            choice = input("Choose an option: ")

            if choice == "1":
                try:
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print(f"Deposit successful. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    print(f"Withdrawal successful. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                account.authenticated = False
                break
            else:
                print("Invalid option. Try again.")