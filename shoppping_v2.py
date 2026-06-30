print("=================Roby Mart===================")
print("")
print("=============Available Products==============")
print("")

products = {
    "soap": {"price": 30, "stock": 20},
    "surf": {"price": 120, "stock": 15},
    "shampoo": {"price": 90, "stock": 12},
    "toothpaste": {"price": 50, "stock": 30},
    "pulses": {"price": 200, "stock": 8},
    "rice": {"price": 70, "stock": 25},
    "wheat": {"price": 45, "stock": 40},
    "sugar": {"price": 55, "stock": 20},
    "salt": {"price": 25, "stock": 35},
    "tea": {"price": 180, "stock": 15},
    "coffee": {"price": 350, "stock": 10},
    "milk": {"price": 60, "stock": 25},
    "curd": {"price": 40, "stock": 20},
    "paneer": {"price": 90, "stock": 12},
    "butter": {"price": 60, "stock": 15},
    "ghee": {"price": 650, "stock": 8},
    "oil": {"price": 180, "stock": 18},
    "biscuits": {"price": 30, "stock": 40},
    "chips": {"price": 20, "stock": 50},
    "noodles": {"price": 25, "stock": 35},
    "maggi": {"price": 18, "stock": 45},
    "cold_drink": {"price": 40, "stock": 30},
    "juice": {"price": 50, "stock": 20},
    "chocolate": {"price": 80, "stock": 25},
    "icecream": {"price": 120, "stock": 15},
    "bread": {"price": 35, "stock": 20},
    "eggs": {"price": 90, "stock": 25},
    "banana": {"price": 60, "stock": 30},
    "apple": {"price": 180, "stock": 18},
    "orange": {"price": 120, "stock": 20}}
for product in products :
 print(f"{product:<11}: ₹{products[product]['price']:<6} Stock: {products[product]['stock']:<2}")
print("")
cart = []
grand_total = 0
while True:
        selected_product = input("enter the product you want to buy(or type done to finish):").lower()
        if selected_product == "done".lower():  
         break

        if selected_product in products:
            print(f"Price: ₹{products[selected_product]['price']:>4}")

            quantity = int(input("enter the quantity of product you selected :"))
            
            if quantity > products[selected_product]["stock"]: 
                print(f"Sorry, we only have {products[selected_product]['stock']} units of {selected_product} available.")  
            else:
                subtotal = products[selected_product]['price'] * quantity
                print(f"Subtotal: ₹{subtotal:>4}")
                cart.append({"product": selected_product,"price": products[selected_product]['price'],  "quantity": quantity})
                grand_total += subtotal
                products[selected_product]["stock"] -= quantity
                print(f"✅ {quantity}x {selected_product} added to cart.")
        else:
            print("invalid product. please try again.")
            

print()
print("=================Roby Mart===================")
print()
print(f"{'Product':<15}{'Qty':<10}{'Price':<10}{'Total':<10}")
print("---------------------------------------------")
bill_total = 0
for item in cart:
    item_total = item["price"] * item["quantity"]
    bill_total += item_total

    print(f"{item['product']:<15}{item['quantity']:<10}{'₹':<0}{item['price']:<10}{'₹':<0}{item_total:<10}")
print("---------------------------------------------")  


print(f"{'Grand Total:':<36}{'₹':<0}{bill_total:<0}")

print()

print("=======Thank you for shopping with us!=======")
print()
print()
print()
print()

    