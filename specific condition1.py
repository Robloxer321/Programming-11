tax = 1.12
item_1 = float(input ("Enter the price of your first item: "))
item_2 = float(input ("Enter the price of your second item: "))
item_3 = float(input ("Enter the price of your third item: "))
price_without_tax = item_1+ item_2 + item_3
print ("Cost before tax %.2f" % price_without_tax)
Cost = price_without_tax*tax
print ("Total cost is %.2f dollars" % Cost)
deposit = float(input ("Please enter the total amount of your purchase"))
if float(deposit) > 50 :
    print (" you have free shipping"
    print  ("Total cost of your purchases is %.2f dollars " % Cost)
if int(deposit) < 50 :
    print ("Shipping will be an extra 10$")
    print  ("Total cost is %.2f dollars" % Cost * float (tax))
print ("Have a nice day")
