#ATM MACHINE Simulates
#TODO = 
#! TASk1 : Display a welcome message for the ATM 
#! TASK2 : Create a variable that stores the initial account balance
#! TASK3 : Use a loop so the ATM Menu Keeps appering until the user chooses to exists
#! TASK4 : Display the ATM options everytime the program runs
#! TASK5 : Ask the user to enter their choice
#! TASK6 : If the user selects check balance. Display the current balance
#! TASK7 : If the user selects Deposit Money.
#! TASK8 : if the user selects withdraw money 
#! TASK9 : If The User Selects Exit. Stop the program and display a thank you message
#! TASK10 : If the user enters any invalid option, display an error message and show the menu again.


balance = 0

while True:
    
    print("\n"  "-------------WELCOME TO ATM MACHINE----------------")
    print("------ATM MENU------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter Your Choice Here: ")

    if choice == "1":
        print("Your Current Balance is:", balance)

    elif choice == "2":
        deposit = float(input("Enter Your Deposit Amount: "))
        balance = balance + deposit
        print("Deposit Successful")
        print("Updated Balance:", balance)

    elif choice == "3":
        withdraw = float(input("Enter Withdrawal Amount: "))

        if withdraw <= balance:
            balance = balance - withdraw
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Thank You For Using ATM")
        break

    else:
        print("Invalid Choice Please Try Again")
