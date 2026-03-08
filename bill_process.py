size = input("Enter Size of Pizza(S/M/L)?")
bill = 0
if size == 'S' or size =='s':
    bill = bill+150
    print(f"Small Pizza Cost is {bill}") 
elif size == 'M' or size =='m':
    bill = bill+250
    print(f"Medium Pizza Cost is {bill}")
else:
    bill = bill+350
    print(f"Large Pizza Cost is {bill}")
Add_pepper = input("Do You Wnat to Add Pepper(Y/N)?")
if Add_pepper == 'y' or Add_pepper =='Y':
    if size == 'S' or size =='s':
        print("Pepper Cost for Small Pizza is 30 Rupees")
        bill = bill+30
    else:
        print("Pepper Cost for Medium/Large Pizza is 50 Rupees")
        bill = bill+50
extra_cheese = input("Do You Wnat to Add Cheese(Y/N)?")
if extra_cheese == 'y' or extra_cheese =='Y':
    print("For Extra Cheese, Cost for All types of Pizza is 50 Rupees")
    bill = bill + 50
print(f"Your Final Bill is {bill}") 