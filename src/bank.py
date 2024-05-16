from .Withdrawal import Withdrawal
from .CurrentAccount import CurrentAccount
from .Deposit import Deposit
from .NaturalPerson import NaturalPerson


def menu():
    return """
    
    menu:

    [1] - Deposit
    [2] - Withdrawal
    [3] - Extract
    [4] - New Account
    [5] - List of accounts
    [6] - New Customer
    [7] - Exit

    =>> """

def bank():
    customers = []

    while True:
        choise = input(menu())

        if (choise == "1"):
            print("Deposit")
            deposit(customers)
            
        elif(choise == "2"):
            print("Withdrawal")
            withdrawal(customers)

        elif(choise == "3"):
            print("Extract")
            extract(customers)

        elif(choise == "4"):
            print("New Account")
            new_account(customers)

        elif(choise == "5"):
            print("List of accounts")
            list_of_accounts(customers)

        elif(choise == "6"):
            print("New Customer")
            new_customer(customers)

        elif(choise == "7"):
            print("Exiting...")
            break

def deposit(customers):
    cpf = input("Enter the CPF(only numbers) of the customer: ")
    customer = find_customer(customers, cpf)

    if customer:
        if list_accounts(customer) > 0:
            account_number = int(input("Enter the account number: "))
            account = find_account(customer, account_number)
            if account:
                value = float(input("Enter the amount you want to deposit: "))
                customer.perform_transaction(account, Deposit(value))
            else:
                print("Account not found")
        else:
            print("Customer has no accounts")
    else:
        print("Customer not found")
    

def withdrawal(customers):
    cpf = input("Enter the CPF(only numbers) of the customer: ")
    customer = find_customer(customers, cpf)

    if customer:
        if list_accounts(customer) > 0:
            account_number = int(input("Enter the account number: "))
            account = find_account(customer, account_number)
            if account:
                value = float(input("Enter the amount you want to withdraw: "))
                customer.perform_transaction(account, Withdrawal(value))
            else:
                print("Account not found")
        else:
            print("Customer has no accounts")
    else:
        print("Customer not found")

def extract(customers):
    cpf = input("Enter the CPF(only numbers) of the customer: ")
    customer = find_customer(customers, cpf)

    if customer:
        if list_accounts(customer) > 0:
            account_number = int(input("Enter the account number: "))
            account = find_account(customer, account_number)
            if account:
                print(f"Extract of the account {account_number}:")
                for transaction in account.history.transactions:
                    print(f"Type: {transaction['type']} - Value: {transaction['value']} - Date: {transaction['date']}")
                print(f"Balance: {account.balance:.2f}")
            else:
                print("Account not found")
        else:
            print("Customer has no accounts")
    else:
        print("Customer not found")

def new_account(customers):
    cpf = input("Enter the CPF(only numbers) of the customer: ")
    customer = find_customer(customers, cpf)

    if customer:
        account = CurrentAccount.new_account(len(customer.accounts)+1, customer)
        customer.add_account(account)
    else:
        print("Customer not found")        

def list_accounts(customer):
    has = len(customer.accounts) # number of accounts
    print(f'Customer {customer.name} has {has} accounts.')
    for account in customer.accounts:
        print(f"type: {account.__class__.__name__} - agency: {account.agency} - number: {account.number} - balance: {account.balance:.2f}")
    return has

def new_customer(customers):
    cpf = input("Enter the CPF(only numbers) of the customer: ")
    name = input("Enter the name of the customer: ")
    birth_date = input("Enter the birth date of the customer: ")
    address = input("Enter the address of the customer: ")

    client = NaturalPerson(cpf, name, birth_date, address)
    customers.append(client)
    print(f"Customer {client.name} created successfully!")

def find_customer(customers, cpf):
    customer = [customer for customer in customers if customer.CPF == cpf]
    return customer[0] if any(customer) else None

def find_account(customer, number):
    account = [account for account in customer.accounts if account.number == number]
    return account[0] if any(account) else None

def list_of_accounts(customers):
    cpf = input("Enter the CPF(only numbers) of the customer: ")
    customer = find_customer(customers, cpf)

    if customer:
        list_accounts(customer)
    else:
        print("Customer not found")
