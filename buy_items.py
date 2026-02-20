
class store_item:
    def __init__(self, name, quantity, price, in_stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.in_stock = in_stock

    def practice_item_choice(self):
        global money
        
        print(f"Item name: {self.name} \n\nThe item price is ${self.price}.00\n")
        if self.in_stock == True:
            print(f"{self.name} is currently in stock.\n")
            ######
            purchase = input("Would you like to purchase this item?").lower()
            if "yes" in purchase and money >= self.price:
                money -= self.price
                print(f"\nYou have purchased a {self.name}!\n")
                print(f"You have ${money}.00 left.\n")
                shopping_cart.append(self.name)
                print(f"SHOPPING CART CONTENTS: \n{shopping_cart}\n")
            if "yes" in purchase and money <= self.price:
                    print("You do not have sufficient funds to purchase this item.")
            if "no" in purchase:
                print("Item not purchased.\n")
        return money

########
######## ACTUAL WORKING CODE BELOW
# if you cut out the next  line then local variable message is not associated with a value
message = ''
money = 100

items = [
     store_item("Book", 100, 12, True),
     store_item("Desk", 100, 40, True),
     store_item("Coffee mug", 100, 10, True),
     store_item("Laptop", 20, 100, True)
        ]

shopping_cart = []

#This, and the route, are they key functions making the buttons work.
def item_choice_made(choice):
    for item in items:
        if item.name.lower() == choice:
            message = f"You have selected: {item.name} \n\n. The item price is ${item.price}.00\n"
            if item.in_stock == True:
                in_stock_query = f". {choice} is currently in stock.\n Would you like to purchase this item?"
                return message + in_stock_query
                # if the user says purchase the item then:
                    #output: return message (replacing above message), saying the item has been purchased, then
                    # append the item to the shopping cart and subtract the cost of the item from the money total
                # elif the user says purchase the item but does not have enough funds:
                # output: return message saying the user does not have enough funds.
            if choice and money >= item.price:
                message = f"{item.name} has been purchased." 
                shopping_cart.append(choice)
            elif choice and money <= item.price:
                message = f"You lack sufficient funds to purchase this item."



     

