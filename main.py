#=======================================ROGRAM IMPUT=======================================#

sale = []
from Sales_Calculation_Function import sales
prosecute = "Y"

print("Welcome, please enter the dsta to register the sale")

#==============================REGISTATION AND SALESS ORDER=================================#

while prosecute.upper() != "N":    
    try:
        item = input("Enter article Name: ")
        price = float(input("Enter Item Price:" ))
        amount = int(input("Quantity of Items Sold: "))
        
        current_sale = {
            "ARTICLE" : item,
            "UNIT_PRICE" : price, 
            "QUANTITY" : amount, 
            "TOTAL" : price * amount  
        }
        sale.append(current_sale)

        sales(price, amount)
    
    except ValueError: 
        print("Pleace enter numeric values in Price and Quality")
        
    prosecute = input("Do you want to register another Sale? (Y/N): ").strip().upper()
    
    continue
        
#===================================SALES SUMMARY===================================#

print("Sale Summary: ")
print(f"{'ARTICLE'}{'UNIT PRICE'}{'QUANTITY'}{'TOTAL'}")

total_sale = 0.0

print("\n" + "="*70)
print(f"{'ARTICLE':<25} {'UNIT_PRICE':>12} {'QUANTITY':>10} {'TOTAL':>12}")
print("-"*70)

for s in sale:
    print(f"{s['ARTICLE']:<25} {s['UNIT_PRICE']:>12,.2f} {s['QUANTITY']:>10} {s['TOTAL']:>12,.2f}")
    total_sale += s['TOTAL']

print("-"*70)
print(f"{'TOTAL OF THE SALE':<55}${total_sale:>12,.2f}")
print("="*70)