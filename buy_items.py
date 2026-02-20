
class store_item:
    def __init__(self, name, quantity, price, in_stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.in_stock = in_stock

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





     

