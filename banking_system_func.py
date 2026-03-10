balance = 0
transactions = []
def login():
    account = input("Enter account number:")
    pin = input("Enter Pin:")
    if account == "1234567" and pin == "111":
        print("Login succesful\n")
        return True
    else :
        print("Invalid Account number or PIN")
        return False
def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    balance+=amount
    transactions.append("Deposited: " + str(amount))
    print("Amount deposited succesfully")
    return balance
def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insuffiecient balance")
    else :
        balance -= amount
        transactions.append("Withdraw: " + str(amount))
        print("Amount Withdraw succcesfully")
        return balance
def show_transactions():
    print("Transaction History:")
    for t in transactions:
        print(t)
if login():
    balance = 0
    while True:
        print("-----Banking Menu-----")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Check Blance")
        print("4.Transactions History")
        print("5.Exit")
        choice = int(input("Enter your chocie: "))
        if choice == 1:
            balance = deposit(balance)
            print("Current balance: ",balance)
        elif choice == 2:
            balance = withdraw(balance)
            print("Current balance: ",balance)
        elif choice == 3:
            print("Current Balance: ",balance)
        elif choice == 4:
            show_transactions()
        elif choice == 5:
            print("***Thank you for using the banking system***")
            break
        else :
            print("Invalid choice")
    