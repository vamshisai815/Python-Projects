#LIBRARY BOOK TRACKER 
#! TASK= Create a python program that works as a simple library book Tracker 
#! The program should perform the following task: 
#TODO:
#?1 Display A Welcome message for the library book tracker 
#?2 Allow the user to add book by entering :
#*Book Title 
#*Author Name
#?3 Store the book information in a list.
#?4 Allow the user to view all books stored in the library 
#?5 Allow the user to search for book by its title
#?6 Show a menu with options such as :
#*Add Book 
#*view Books
#*Search book 
#*Exit 
#?7 After completing an operation should ask the user if they want to continue 
#?8 IF the user choose yes the program should show the menu again 
#?9 if the user choose no or exit the program should stop running 

print("---------------WELOCOME TO-------------------")
print("---------LIBRARY BOOK TRACKER-----------------")
books =[]

while True:
    print("\n""MENU")
    print("1. Add Book")
    print("2. View Book")
    print("3. Search Book")
    print("4. Exit")

    choice= input("Enter Your Choice Here: ")

    if choice == "1":
        title = input ("Enter The Title of Book: ")
        author = input("Enter The Author Name: ")
        book= {"title":title,"author":author}
        books.append(book)
        print("Book Added Successfully")


    elif choice == "2":
        if len(books)==0:
            print("No Book Available in Library")
        else:
            print("\n""Book List")
            for book in books:
                print(book["title"],"-",book["author"]) 
                
    elif choice=="3":
      search = input("Enter The Title of the book You want to search: ")
      found = False
      for book in books:
          if book["title"].lower() == search.lower():
              print("Book Found",book["title"],"-",book["author"])
              found==True

    if found==False:
        print("Book Not Found")

    elif choice=="4":
        print("Thank You For Using Library Tracker")
        break

    else:
        print("invalid Choice")

    continue_choice = input("Want To Continue (yes/no:): ")
    if continue_choice.lower()!="yes":
        print("Program Ended")
        print("Thank You For Using Library Book Tracker")
        break

