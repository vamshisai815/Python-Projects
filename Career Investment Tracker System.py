#* PART 1 :
#! PROJECT TASk =
#TODO = 
#* Build a system that :
#?1 Takes your name
#?2 Stores Career goal (String)
#?3 Uses a tuple for fixed platforms
#?4 Uses dictionary to store skill + cost 
#?5 Uses list to store all costs
#?6 Uses set to store unique skills
#?7 Calculates total investment 
#?8 Shows Summary 

Name = input("Enter Your Name here :")
Career_Goal = input("Enter Your Carrer Goal :")
Platform = ("Youtube","Udemy", "Coursera","Simple learn")
skills = { 
    "Python" : 3000,
    "SQL" : 5600,
    "Javascript" : 8000,
    "DSA ": 3400
} 

# List to Store All Costs
cost_list = list(skills.values())

# set to store unique skills
unique_skills = set(skills.keys())

# Calculates total investment 
total_investment = sum(cost_list)


print("\n------ Career Investment Summary ------")
print("Name of the Student",Name)
print("Career Goal of the Student",Career_Goal)
print("The Available Platforms are :", Platform)
print("The skils Student Planned :",unique_skills)
print("The Cost for the skills are",cost_list)
print("The total Inverstment is :",total_investment)
print("\n--------------------👍😊ALL THE BEST😊👍----------------------------")
print("\n --------------------🌟🌟🌟KEEP SHINEING🌟🌟🌟-----------------------")