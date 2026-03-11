inventory ={}
def add_product():
    name = input("Enter name of the product:")
    quantity =int(input("Enter Quantity:"))
    price = int(input("Enter Price:"))
    inventory[name] = [quantity,price]
    print("Product added successfully")
def update_quantity():
    name = input("Enter product name to update:")
    if name in inventory:
        new_quantity = int(input("Enter New Quantity:"))
        inventory[name][0]=new_quantity
        print("Quantity updated successfully")
    else:
        print("Product not found")
def remove_product():
    name = input("Enter name of the product to delete :")
    if name in inventory:
        del inventory[name]
        print("Product removed")
    else :
        print("Product not found")
def total_value():
    total = 0
    for item in inventory:
        quantity = inventory[item][0]
        price = inventory[item][1]
        total = total + quantity*price
    print("Total Inventory Value:",total)
def low_stock():
    for item in inventory:
        if inventory[item][0] < 10:
            print(item, "-","quantity:",inventory[item][0])
while True:
    print("----Inventory Menu----")
    print("1.Add Product")
    print("2.Updated Product")
    print("3.Remove Product")
    print("4.Display Total Inventory Value")
    print("5.Display Low Stock Product")
    print("6.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_product()
    elif choice == 2:
        updated_product()
    elif choice == 3:
        remove_product()
    elif choice == 4:
        total_value()
    elif choice == 5:
        low_stock()
    elif choice == 6:
        print("Program Ended")
        break
    else :
        print("Invalid Choice")
        
        
    
    
    
    