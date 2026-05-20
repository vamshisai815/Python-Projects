#BASIC CALCULATOR 
#?Project objective =
#?Bulid a simple calcualtor system that take:
#* Takes two numbers from the user and perform mathematical operation and display caculatio result 
#TODO= Task list
#!1 Show welcome message and calculator title 
#!2 Ask user to enter the first number 
#!3 Ask user to enter the second number 
#!4 Show operation choices:
#!Addition 
#!Subtraction
#!Multiplication 
#!Division 
#!5 Ask the user to select operation 
#!6 Use condition to check selected operation 
#!7 Store final answer in a variable 
#!8 show Entered numbers and selected operation and final answer 
#!9 Check whether user entered correct operation choice 
#!10 Display thank you message

#!Let's Start The Project 

#*Welcome Message 
print("--------------- (●'◡'●) Welcome To The Calcuator (●'◡'●) -----------------")

#* Ask User To enter the values 

num1= float(input("Enter Your First Number: "))
num2= float(input("Enter Your Second Number: "))

#*Enter Your Choice 
print("\n")
print("-------- SELECT OPERATION ------------")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

#* User Choice 

choice= input("Enter Your Choice(1/2/3/4): ")

#*Use condition 
if choice=="1":
    result= num1 + num2
    operation = "Addition"

elif choice=="2":
    result = num1-num2
    operation= "Subtraction"

elif choice == "3":
    result= num1*num2
    operation = "Multiplication"

elif choice=="4":
    if num2 !=0:
        result = num1/num2
        operation = "DIvision"
    else :
        result= "Cannot Divide by Zero"
        operation = "Division"
else:
    result = "Invalid Choice"
    operation= "Unknown"


#* Display Result 
print("\n")
print("============================= CALCULATION RESULT ===============================")
print("First Number:",num1)
print("Second Number:",num2)
print("Operation:",operation)
print("Result:",result)

#*Thank You Message 
print("\n")
print("========================== THANK YOU FOR USING CALCULATOR =========================")
