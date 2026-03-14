#Employment Profile Generator 
# TODO = TASKS 
#! TASK1; Display Program Title  
#! TASK2: Ask user for employee information
#! TASK3 : Create a dictionary 
#! TASK4 : Determine Employee level
#! TASK5 : Add level to dictioanry 
#! TASK6 : Generate Employee Profile

print("\n" "---------------WELLCOME TO--------------------")
print( "------------EMPLOYEE PROFILE GENERATOR------------")

Employee_ID =input("Enter Your Employee ID: ")
Employee_Name = input("Enter YOur Name: ")
Employee_Age = input("Enter Your Age: ")
Employee_Email = input("Enter Your Email: ")
Employee_Department = input("Enter Your Department: ")
Employee_Salary = input("Enter Your Salary: ")
Employee_Experience = float(input("Enter Your Experience: "))


if Employee_Experience <2:
    print("The Employee Is Fresher")
elif Employee_Experience<=5:
    print("The Employee is junior")
elif Employee_Experience<=10:
    print("The Employee is Senior")
else:
    print("The Employee is Expert")

Employee = {
    "ID":Employee_ID,
    "Name": Employee_Name,
    "Age": Employee_Age,
    "Email": Employee_Email,
    "Department":Employee_Department,
    "Salary":Employee_Salary,
    "Experience":Employee_Experience 
    } 

print("\n""---------------EMPLOYEE PROFILE------------------")
print("Employee ID: ",Employee["ID"])
print("Employee Name: ",Employee["Name"])
print("Employee Age: ",Employee["Age"])
print("Employee Email: ",Employee["Email"])
print("Employee Department: ",Employee["Department"])
print("Employee Salary: ",Employee["Salary"])
print("Employee Experience: ",Employee["Experience"])
print("\n""--------------KEEP IT UP -----------------")
print("\n""--------------THANK YOU-------------------")


