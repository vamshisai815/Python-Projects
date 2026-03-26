# STUDENT RESULT ANALYZER 
#! Take a name and 3 subject marks 
#! Calculate Total Marks 
#! Calculate Percentage
#! Check if any subject<35 yes fail 
#! else pass 
#! Grade Logic
#! if>=90 = A
#! if>=75 = B
#! if >=50 = C
#! else + D
#! Display All results 

Name = input("Enter Your Good Name: ")
Business_Accounts = float(input("Enter Your Marks in Businesss Accounts: "))
Business_Economics = float(input("Enter Your Marks in Business Economics: "))
Business_Law = float(input("Enter Your Marks in Business law "))

Total_Marks = Business_Accounts + Business_Economics + Business_Law

Percentage = Total_Marks/3

if Business_Accounts<35 or Business_Economics<35 or Business_Law<35 :
    result= "Fail"
else:
    result = "Pass"

#? Grade 

if Percentage>=90:
    print("Grade A")
elif Percentage>=75:
    print("Grade B")
elif Percentage>50:
    print("Grade C")
else :
    print("Grade D")

print("------------------RESULT-----------------")
print("Name of The Student :",Name )
print("Total Marks of The Student",Total_Marks)
print("Total Percentage : ",Percentage)
print("FInal Result: ",result)
