#STUDENT AND INTERSHIP SKILL TRACKER 
#TODO = 
#!Task1 :
#*Create 3 Variablles
#? student_name 
#? Course
#?future_goal 
#? print them 

#! Task2 :
#? Create:
#! One empty dictionary for interships 
#! One Empty set for skills 
#  Task 3:
# Create a while True loop and show menu:

# 1. Add Skill
# 2. Apply Internship
# 3. Update Status
# 4. Show Data
# 5. Exit

# Take input from user.

#  Task 4:
# If user selects:
# Option 1
# Take skill input
# Add to set
# Option 2
# Take company name
# Take role
# Store in dictionary using tuple (role, status="Applied")
# Option 3
# Ask company name
# If exists → update status
# Option 4
# Print all skills
# Print all internship details using loop
# Option 5
# Break loop

student_name= "Akash Tiwari"
Course = "Bachlors in Commerce"
future__Goal = "CA"
print("\n" "-----------------WELCOME--------------------------------")
print("Name=",student_name)
print("Course Enrolled =",Course)
print("The Student want to become =", future__Goal)
print("-------------------------------------------------------------")

intership = {} 
skills = ()

while True:
    print ("\n" "Add Skills")
    print ("Apply Intership")
    print("Update Status")
    print("Show Data")
    print("Exit")
    choice = input("Enter Choice:") 

    if choice=="1":
        skills = input("Enter Your skills : ")
        
        print("skills added successfully")

    elif choice == "2":
        company_name = input("Enter Your Company name:")
        Role = input("Enter Your Role : ")
        intership[company_name] =(Role,"Applied") 
        print("Internship Applied!") 

    elif choice == "3":
     company = input("Enter company name to Update :")
     if company in intership:
        role = intership[company[0]]
        new_status = input("Enter New Status:")
        intership[company]= (role,new_status)
        print("Status Updated!")

    else :
       print("Company Not Found!")

    
    if choice == 4 :
       print("\n--- Skills ---")
       for s in skills:
          print(s)
          
          print("\n--- Internships ---")
          for company, details in intership.items():
             print("Company:", company)
             print("Role:", details[0])
             print("Status:", details[1])
             print("----------------")
             
    elif choice == "5":
       print("Exiting program...")
       break
    # else:
    #     print("Invalid choice!")