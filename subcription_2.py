print("Available OTT Platforms")
print("1. Netflix - Rs.499")
print("2. Amazon Prime - Rs.399")
print("3. Disney+ Hotstar - Rs.299")
print("4. AHA - Rs.199")
print("5. Zee5 - Rs.149")
count = int(input("\nHow many OTT platforms do you want to select (1/2/3)? "))
# Validation for OTT count
if count > 3:
    print("You can select only up to 3 OTT platforms at a time...!")
else:
    total_amount = 0
    # Select OTT platforms
    for i in range(1,count+1) :
        choice = int(input(f"Select OTT {i} (Enter number): "))
        if choice == 1:
            total_amount += 499
        elif choice == 2:
            total_amount += 399
        elif choice == 3:
            total_amount += 299
        elif choice == 4:
            total_amount += 199
        elif choice == 5:
            total_amount += 149
    # Discount logic
    if count == 1:
        discount_rate = 0
    elif count == 2:
        discount_rate = 0.30
    elif count == 3:
        discount_rate = 0.40
    discount_amount = total_amount * discount_rate
    amount_after_discount = total_amount - discount_amount # final amount
    # GST calculation
    gst_amount = amount_after_discount * 0.20
    final_amount = amount_after_discount + gst_amount
    # Output
    print("\n------ BILL SUMMARY ------")
    print("Number of OTTs Selected:", count)
    print("Base Amount: Rs.", total_amount)
    print("Discount Amount: Rs.", discount_amount)
    print("GST Amount (20%): Rs.", round(gst_amount))
    print("Final Payable Amount: Rs.", round(final_amount))