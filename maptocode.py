class ATM:
    def __init__(self, location, branchName):
        self.location = location
        self.branchName = branchName

    def show(self):
        return f"ATM Location: {self.location}, Branch: {self.branchName}"


class User:
    def __init__(self, cardNumber, PIN, accountBalance):
        self.cardNumber = cardNumber
        self.PIN = PIN
        self.accountBalance = accountBalance

    def validate_PIN(self, inputPIN):
        return self.PIN == inputPIN


class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deduct_amount(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False


class CashDispenser:
    def __init__(self, availableCash):
        self.availableCash = availableCash

    def dispense_cash(self, amount):
        if amount <= self.availableCash:
            self.availableCash -= amount
            return True
        else:
            return False


class Transaction:
    def __init__(self):
        self.transactionLog = []

    def generate_transaction(self, transactionID, amount, status):
        self.transactionLog.append({
            "Transaction ID": transactionID,
            "Amount": amount,
            "Status": status
        })

    def log_transaction(self):
        return self.transactionLog


# Withdraw Code
def withdraw_cash(user, bankAccount, dispenser, amount):
    if amount > bankAccount.check_balance():
        return "Error: Insufficient funds."
    if not dispenser.dispense_cash(amount):
        return "Error: ATM out of cash."
    
    bankAccount.deduct_amount(amount)
    return f"Withdrawal successful. Remaining balance: ${bankAccount.check_balance()}."


# Customer Sample
atm = ATM("Downtown", "Main Branch")
user = User("1234567890", "1234", 500)
bank_account = BankAccount("987654321", 500)
cash_dispenser = CashDispenser(1000)

# Validate PIN & Withdraw Cash
inputPIN = "1234"
if user.validate_PIN(inputPIN):
    print("PIN validated.")
    amount_to_withdraw = 200
    print(withdraw_cash(user, bank_account, cash_dispenser, amount_to_withdraw))
else:
    print("Invalid PIN.")
