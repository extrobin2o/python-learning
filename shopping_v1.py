print("=======roby mart=======")
print("")
print("======available products======")
print("")

products = {"surf":120,"soap":30, "shampoo":90, "toothpaste":50, "pulses":200}
subtotal = 0
subtotal2 = 0

for product in products:
    print(product,": ₹",products[product])
selected_product = input("enter the product you want to buy:")
if selected_product in products:
    price = products[selected_product]
    print("Price: ₹", price)
    enter_quantity = int(input("enter the quantity of product you selected :"))
    subtotal = price*enter_quantity
else:
    print("Product not available")
further_reqirement = input(" anything else you want to buy? (yes/no):")
if further_reqirement == "yes":
    selected_product2 = input("enter the product you want to buy more:")
    if selected_product2 in products:
            price2 = products[selected_product2]
            print("Price: ₹", price2)
            enter_quantity2 = int(input("enter the quantity of you second product:"))
            subtotal2 = price2*enter_quantity2
    else:
        print("Product not available")
else:print("Thank you for shopping with us!")        
print("")
print("====BILL====")
print("")
print("Subtotal of first product:", subtotal)
print("Subtotal of second product:", subtotal2)
print("")
print("Grand_total :", subtotal+ subtotal2) 
print("")
print("Thank you for shopping with us!")