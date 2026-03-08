total_seats = 40
discount = 0.0
seats_required = int(input("Enter number of seats required: "))
if seats_required == 1:
    age = int(input("Enter Passenger Age: "))
    ticket_type = input("Enter ticket type (AC / Non-AC): ").upper()
    ac_price = 800
    non_ac_price = 500
    if seats_required <= total_seats:

        if ticket_type == "AC":
            base_fare = ac_price * seats_required
        else:
            base_fare = non_ac_price * seats_required
        if age >= 5 and age <= 12:
            discount = 0.50
            print(f"Your discount(50%) Amount = {base_fare * discount}")
        elif age > 12 and age <= 18:
            discount = 0.20
            print(f"Your discount(20%) Amount = {base_fare * discount}")
        elif age > 18 and age <= 60:
            discount = 0.0
            print(f"Your discount(0%) Amount = {base_fare * discount}")
        else:
            discount = 0.30
            print(f"Your discount(30%) Amount = {base_fare * discount}")

        fare = base_fare - (base_fare * discount)

        print("Booking Confirmed")
        print("Total Ticket Cost:", fare)
    else:
        print("Booking Not Confirmed, Not Enough Seats Available!")
else:
    print("Select Only One Ticket, Thank You!")