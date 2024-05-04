menu = """

[1] - Deposit
[2] - Withdrawal
[3] - Statement
[4] - Exit

=>> """

balance = 0
limit = 500
statement = ""
withdrawal_amount = 0
WITHDRAWAL_LIMIT = 3

while True:
    choise = input(menu)

    if (choise == "1"):
        deposit = float(input("Enter the amount you want to deposit: "))
        
        if (deposit > 0 ):
            balance += deposit
            statement += f"\nDeposit: R$ {deposit:.2f}" 
        else:
            print("Invalid Value")
        
    elif(choise == "2"):
        withdrawal = float(input("Enter the amount you want to withdraw: "))
        if(withdrawal > 0):
            if(withdrawal_amount >= WITHDRAWAL_LIMIT):
                print("You have reached the withdrawal limit")
            elif(withdrawal > limit):
                print("Withdrawal limit exceeded")
            elif(withdrawal <= balance):
                balance -= withdrawal
                statement += f"\nWithdrawal: R$ {withdrawal:.2f}"
                withdrawal_amount += 1
            else:
                print("Insufficient Funds")
        else:
            print("Invalid Value")

    elif(choise == "3"):
        print(f"Satement: \n{statement}\n\n")
        print(f"Balance: R$ {balance:.2f}")

    elif(choise == "4"):
        print("Exiting...")
        break

    else:
        print("Invalid Option")