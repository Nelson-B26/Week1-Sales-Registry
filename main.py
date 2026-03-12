#PROGRAM IMPUT
from Sales_Calculation_Function import sales

print("Welcome, please enter the dsta to register the sale")

try:
    item = input("Enter article Name: ")
    price = float(input("Enter Item Price:" ))
    amount = int(input("Quantity of Items Sold: "))
    
    sales(price, amount)
        
except:
    print("Pleace enter numeric values in Price and Quality")