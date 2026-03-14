#Student expense And Saving Tracker 
#(Based only on varibales and data types)
#you are a student and you want tyo track your monthly money 
#Task 1 store the Following details using variables 

student_name = "Vachan Sharma"
student_course = "B.COM"
monthly_pocket_money = 20000 #in INR

# Task 2 Store Monthly Expenses
food_expense = 3000
travel_expense = 2000
internet_expense = 4000 
study_material_expense = 2500
hostel_fees = 4500
additional_expenses = 3500

#Task 3 Calculate

total_monthly_expenses = (food_expense + travel_expense + internet_expense + study_material_expense + hostel_fees + additional_expenses)
saving= monthly_pocket_money-total_monthly_expenses

#Task 4 calculate the expense percentage of pocket money
expense_percentage = (total_monthly_expenses/monthly_pocket_money)*100

#Task 5 display all details in a clean format 
print("The student name is", student_name)
print("The Student is study in", student_course)
print("The monthly pocket money is INR", monthly_pocket_money)
print("The total monthly expenses are INR", total_monthly_expenses)
print("The saving of the student is", saving)
print("so the expense percentage of the student is", expense_percentage)

