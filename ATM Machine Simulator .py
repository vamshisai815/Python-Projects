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


print("----------- WELCOME TO ATM MACHINE -----------")

balance = 1000

while True:

    print("\n------ ATM MENU ------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Money deposited successfully")
        print("New balance:", balance)

    elif choice == "3":
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")

    continue_choice = input("Do you want to continue? (yes/no): ")

    if continue_choice.lower() != "yes":
        print("Thank you for using ATM")
        break


