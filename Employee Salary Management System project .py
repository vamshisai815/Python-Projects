#TASK (Projecct overview)
#Problem Statement
# Create a program for a company accounts department that :
#1 Takes Employee details:
#A Employee Name
#B Emloyee ID
#C Department

#2 Takes Salary Details:
#A Basic Salary 
#B HRA
#C DA

#3 Calculates:
# Gross Salary 
# Tax(5%)
# Net Salary 

#4 Displays a complete salary slip 

# Employee Details

Employee_name = "Yuvraj Yadav"
Employee_ID = "EP121"
Department = "Finance Department"

# Salar Details 

basic_salary = 40000
HRA = 20000
DA = 40000

# Calculates:

gross_salary = basic_salary + HRA + DA
tax= gross_salary*5/100
net_salary = gross_salary-tax

#Complete Salary Slip

print("The name of the employee is",Employee_name)
print("The ID of Employee",Employee_ID)
print("The employee from",Department)
print("The Employee can got the basic salary",basic_salary)
print("The Employee have also got the HRA ",HRA)
print("The Employee have also got the DA", DA)
print("The Gross salary of the employee",gross_salary)
print("The 5% Tax Paid by emplyee",tax)
print("The net salary of the employee",net_salary) 


