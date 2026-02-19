money = 100

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

shopping_cart = []

########
######## ACTUAL WORKING CODE BELOW

items = [
     store_item("Book", 100, 12, True),
     store_item("Desk", 100, 40, True),
     store_item("Coffee mug", 100, 10, True),
     store_item("Laptop", 20, 100, True)
        ]

#This, and the route, are they key functions making the buttons work.
def item_choice_made(choice):
    for item in items:
        if item.name.lower() == choice:
            message = f"You have selected: {item.name} \n\n. The item price is ${item.price}.00\n"
            if item.in_stock == True:
                in_stock_query = f". {choice} is currently in stock.\n"
    return message + in_stock_query + purchase_option()


def purchase_option():
            return f"Would you like to purchase this item?"

def purchase_choice_made(purchase_choice):
        if purchase_choice: # and money >= self.price:
             #   money -= self.price
                purchase_message = f"\nYou have purchased a {item.name}!\nYou have $100.00 left.\n"
                return purchase_message
                 

