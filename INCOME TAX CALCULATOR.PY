# INCOME TAX CALCULATOR
#TODO = 
#! TASK1 : Take uer details
#! TASK2 : Store Data
#! TASK3 : Create tax Slabs 
#! TASK4 : Create a function 
#! TASK5 : Create a list to store multiple users income
#! TASK6 : Use Loop to allow multiple users to calculate tax 
#! TASK7 : Print a tax summary 
#! TASK8 : Store tax slabs in tuples 
#! TASK9 : Use a set to store unique cities of users

Tax_Slabs = (25000,50000,1000000)

income_list = []
cities = set()
def calculate_tax(income):
    if income<=25000:
        tax=0 
    elif income <= 50000:
        tax = income*0.05
    elif income <= 100000:
        tax = income*0.20
    else:
        tax= income*0.30
    return tax

while True:
    Name = input("Enter Your Name: ")
    Age= int(input("Enter Your Age: "))
    income= float(input("Enter Your Income: "))
    City = input("Enter Your City: ")
    
    income_list.append(income)
    cities.add(City)
    tax = calculate_tax(income)
    

    print("\n" "-------------TAX SUMMARY--------------")
    print("Name: ", Name)
    print("Age:",Age)
    print("Income:",income)
    print("Tax To Pay:",tax)

    choice = input("Do You Want to calculate tax for another user? (yes/No)")
    if choice.lower() != "yes":
        break

print("\n" "All Incomes:",income_list)
print("Cities:",cities)
print("Tax Paid:",tax)
print("-------------------THANK YOU FOR USEING INCOME TAX CALCULATOR -----------------------")





  

        

