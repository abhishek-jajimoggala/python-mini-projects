#ATM application
while True:
    account=100000
    card=input("Insert the card:")
    pwd=int(input("Enter the password:"))
    if card=="C":
        print("Welcome Abhishek")
        if pwd==1234:
            option=int(input("choose your options 1.Balance enquery 2.Withdraw"))
            if option==1:
                print("Your Account Balance is:",account)
            elif option==2:
                a=int(input("Enter the amount to withdraw:"))
                print(account)
                remaining_balance=(account-a)
                print("Remaining balance is:",remaining_balance)
        else:
           print("Invalid password")
    else:
        print("Please insert the card Properly")
                
