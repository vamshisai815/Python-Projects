#MOBILE RECHARGE SYSTEM 
#TODO= Task List 
#?1 Show Welcome message and recharge system title. 
#?2 Ask The user to enter their details 
#?3 Convert Recharge amount into numeric format 
#?4 Check recharge category using recharge amount 
#?5 Store all recharge information together
#?6 Display all recharge details clearly 
#?7 Display messages based on recharge amount 
#?8 Display Thank you message before ending system 


#! Welcome message 

print("\n" "=============== 🙏🙏 WELCOME TO THE MOBILE RECHARGE SYSTEM 🙏🙏 =============== ")

#! User Details and Type converison 
print("\n""Please Fill Your Detils")
Name =input("Enter Your Name: ")
Mobile_no= int(input("Enter Your Mobile Number: "))
Service_Provider=input("Enter Your Service Provider: ")
Recharge_Amount= float(input("Enter The Recharge Amount per month: "))

#! Check Recharge Plan 
if Recharge_Amount<199:
    Recharge_plan= "Small Recharge Plan"
elif Recharge_Amount<=399:
    Recharge_plan= "Medium Recharge Plan"
else:
    Recharge_plan= "Preimum Recharge Plan"

#! Store Recharge Details 

Recharge= {
    "Name": Name,
    "Mobile No": Mobile_no,
    "Service Provider": Service_Provider,
    "Recharge Amount":Recharge_Amount,
    "Recharge Plan" : Recharge_plan
}

#! Recharge Summery 
print("==============📃 Recharge Summery 📃==================")
print("Name:",Recharge["Name"])
print("Mobile Number:",Recharge["Mobile No"])
print("Service Provider:",Recharge["Service Provider"])
print("Recharge Amount:", Recharge["Recharge Amount"])
print("Recharge Plan:",Recharge["Recharge Plan"])

#! Additional Message 

if Recharge_Amount>499:
    print("🎉Congratulations You Received Unlimited Data Pack with our Unlimited Calls")
elif Recharge_Amount>399:
    print("💰Congratulations You Received 1.5GB Data and Unlimited Calls")
else:
    print("📱Congrutulations You Received Unlimited Calls")

#! Thank You Message
print("\n""==============🙏Thank You For Using Our System 🙏============")

#! Review
review =float(input("Please Give A Review: "))
opinion= input("Suggest Your Opinon Which Help Us To improve Our System: ") 
print(review,"and",opinion)
print("========= 😊Thank You Reviewing and Share Your Thoughts 😊===============")

