#Password Manager Program
details = {}
def add_password():
    website_name =input("Enter website name:")
    username = input("Enter userame:")
    password = input("Enter password:")
    details[website_name] = [username,password]
    print("Password saved succesfully")
def search_password():
    name = input("Enter Website:")
    if name in details:
        print("username:",details[name][0],",""password:",details[name][1])
    else :
        print("website not found")
def view_all():
    print(details)
while True:
    print("---Menu---")
    print("1.Add New Passowrd")
    print("2.Search Password")
    print("3.View all accounts")
    print("4.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_password()
    elif choice == 2:
        search_password()
    elif choice == 3:
        view_all()
    elif choice ==4:
        print("Programm Closed")
        break
    else :
        print("Invalid Choice")
        
    
    