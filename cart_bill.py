cart=[]
n= int(input("Enter no.of tems you want:"))
total_cost=0
cost=0
for i in range(1,n+1) :
    item , quantity , price =input(f"Enter {i} item quantity price: ").split()
    cart.append((item,int(quantity),int(price)))
for item , quantity,price in cart :
    cost=quantity*price
    total_cost+=cost
print(f"Total cost of your shopping is :{total_cost}")