
class store_item:
    def __init__(self, name, quantity, price, in_stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.in_stock = in_stock

# if you cut out the next  line then local variable message is not associated with a value

items = [
# Office & Home goods section
     store_item("Book", 100, 12, True),
     store_item("Desk", 100, 40, True),
     store_item("Coffee mug", 100, 10, True),
     store_item("Bed", 20, 100, True),
# Grocery section
     store_item("Meat", 2, 20, True),
     store_item("Cereal", 40, 4, True),
     store_item("Fruit", 10, 1, True),
     store_item("Milk", 10, 2, True),
# Tech section
     store_item("Mouse", 1, 20, True),
     store_item("Charger", 2, 30, True),
     store_item("Router", 2, 85, True),
     store_item("Laptop", 2, 100, True),

        ]

shopping_cart = []
message = ''






     

