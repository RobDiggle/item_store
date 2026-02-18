money = 100

class store_item:
    def __init__(self, name, quantity, price, in_stock):
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"
        
        self.name = name
        self.quantity = quantity
        self.price = price
        self.in_stock = in_stock

    def item_info(self):
        global money
        
        print(f"Item name: {self.name} \n\nThe item price is ${self.price}.00\n")
        if self.in_stock == True:
            print(f"{self.name} is currently in stock.\n")
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



book = store_item("Book", 100, 12, True)
desk = store_item("Desk", 100, 40, True)
coffee_mug = store_item("Coffee mug", 100, 10, True)
laptop = store_item("Laptop", 20, 100, True)
shopping_cart = []

book.item_info()
desk.item_info()
coffee_mug.item_info()
laptop.item_info()
