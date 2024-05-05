def menu():
    return """

    menu:

    [1] - Deposit
    [2] - Withdrawal
    [3] - Statement
    [4] - New Account
    [5] - List of accounts
    [6] - New user
    [7] - Exit

    =>> """

def main():
    AGENCE = "0001"
    WITHDRAWAL_LIMIT = 3

    balance = 0
    limit = 500
    statement = ""
    withdrawal_amount = 0
    users = []
    accounts = []

    while True:
        choise = input(menu())

        if (choise == "1"):
            value = float(input("Enter the amount you want to deposit: "))
            
            balance, statement = deposit(balance, value, statement)
            
        elif(choise == "2"):
            value = float(input("Enter the amount you want to withdraw: "))
            
            balance, statement, withdrawal_amount = withdrawal(balance=balance, value=value, statement=statement, limit=limit, withdrawal_amount=withdrawal_amount, WITHDRAWAL_LIMIT=WITHDRAWAL_LIMIT)

        elif(choise == "3"):
            extract(balance, statement=statement)

        elif(choise == "4"):
            number_account = len(accounts) + 1

            account = new_account(AGENCE, number_account, users)
            
            if account:
                accounts.append(account)

        elif(choise == "5"):
            list_accounts(accounts)

        elif(choise == "6"):
            new_user(users)

        elif(choise == "7"):
            print("Exiting...")
            break

        else:
            print("Invalid Option")

def deposit(balance, value, statement, /):
    if (value > 0 ):
        balance += value
        statement += f"\nDeposit: R$ {value:.2f}" 
    else:
        print("Invalid Value")

    return balance, statement

def withdrawal(*, balance, value, statement, limit, withdrawal_amount, WITHDRAWAL_LIMIT):
    if(value > 0):
        if(withdrawal_amount >= WITHDRAWAL_LIMIT):
            print("You have reached the withdrawal limit")
        elif(value > limit):
            print("Withdrawal limit exceeded")
        elif(value <= balance):
            balance -= value
            statement += f"\nWithdrawal: R$ {value:.2f}"
            withdrawal_amount += 1
        else:
            print("Insufficient Funds")
    else:
        print("Invalid Value")

    return balance, statement, withdrawal_amount

def extract(balance,/,*, statement):
    print(f"Statement: \n{statement}\n\n")
    print(f"Balance: R$ {balance:.2f}")

def new_account(ACENCY, number_account, users):
    cpf = input("Enter the CPF(only numbers): ")

    if any(user["cpf"] == cpf for user in users):
        print("New account created")
        return {"acency": ACENCY, "number_account": number_account, "cpf": cpf}
    
    print("User not found")    

def list_accounts(accounts):
    for account in accounts:
        print(f"Account: {account['acency']} - {account['number_account']} - {account['cpf']}")    

def new_user(users):
    cpf = input("Enter the CPF(only numbers): ")
    # users = [{"name": "gabriel", "cpf": "1"}]
    if any(user["cpf"] == cpf for user in users):
        print("User already registered")
        return

    name = input("Enter the name: ")
    date_of_birth = input("Enter the date of birth: ")
    address = input("Enter the address: (street - number - neighborhood - city/state):")

    users.append({"name": name, "date_of_birth": date_of_birth, "cpf": cpf, "address": address})

    print("User successfully registered")


if __name__ == "__main__":
    main()