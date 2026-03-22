#CALCULATOR
#TODO= 
#!1 Create a loop using while TRUE
#!2 Display Calculator title 
#!3 Take Two numbers as input 
#!4 Show list of operations 
#!5 Take User Chocie
#!6 Check Choice using if-elif
#!7 perform selected calculation 
#!8 Display result 
#!9 Handle invalid input using else 
#!10 use continue to restart on wrong input 
#!11 Ask user to continue 
#!12 use break to exit program 

print("\n""--------SIMPLR CALCULATOR----------")


while True:
    
    number1= float(input("Enter Your First Number: "))
    number2=float(input("Enter Your Second Number: "))
    
    print("\n""---CHOOSE OPERATION:----")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3>Multiplication(*)")
    print("4.Divison(/)")

    choice= int(input("Enter Your Choice(1/2/3/4): "))

    if choice==1:
        print("Result: ",number1 + number2)

    elif choice==2:
        print("Result:",number1-number2)
    
    elif choice==3:
        print("Result: ",number1*number2)
    
    elif choice==4:
        if number2!=0:
            print("Result: ",number1/number2)

        else:
            print("Cannot Divide by Zero")
            
    else:
        print("Invalied Choice Try Again")
        continue

    

    continue_Choice= input("\n""Do Want to Calucate Again (yes/no) : ").lower()

    if continue_Choice != "yes":
        print("Calucator Closed")
        print("Thank You For Using")
        break
