print("Please Insert Your Card")

password=1818
pin=int(input("please enter your PIN:"))
balance=10000
if pin == password:
    print("Welcome To ATM Simulator")
    print("""
          1 == Check balance
          2 == Withdraw Money
          3 == Deposit Money
          4 == Exit
          """)

    option=int(input("please enter your choice:"))
    if option==1:
        print("Your current balance is:",balance)

    if option==2:
        withdrawl_money=int(input("Enter the amount you want to Withdrawl:"))
        balance=balance-withdrawl_money
        print(withdrawl_money,"is debited from your account")
        print("your current balance is:",balance)

    if option==3:
        deposit_money=int(input("Enter the amount you want to deposit:"))
        balance=balance+deposit_money
        print(deposit_money,"is credited in your account")
        print("your current balance is:",balance)

    if option==4:
        print("Thank you for using the ATM simulator")

else:
    print("Invalid PIN,please try again")


