tax = 1.12
item_1 = float(input ("Enter the price of your first item: "))
item_2 = float(input ("Enter the price of your second item: "))
item_3 = float(input ("Enter the price of your third item: "))
price_without_tax = item_1+ item_2 + item_3
print ("Cost before tax %.2f" % price_without_tax)
Cost = price_without_tax*tax
print ("Total cost is %.2f dollars" % Cost)
