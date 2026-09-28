from exceptions import NotEnoughStockError 
class Product:
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
    def sell(self, amount):
        if amount <= 0:
            raise ValueError("Quantity to sell must be greater than zero.")
        if amount > self.quantity: 
            raise NotEnoughStockError(f"No hay suficiente stock de '{self.name}'.")
        self.quantity = self.quantity - amount
        print(f"Product '{self.name}' sold successfully")
              
    def get_info(self):
        return (f"Name: {self.name} | Code: {self.code} | Price: {self.price} | Quantity: {self.quantity}")
                                
        
class Inventory:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product (self, product):
        for existing_product in self.products:
            if existing_product.code.lower() == product.code.lower():
                print(f"Product code '{product.code}' already exists.")
                return
        self.products.append(product)
        print(f"Product '{product.name}' successfully added to '{self.name}'.")
    def sell_product (self, code, amount):
        for product in self.products:
            if product.code.lower() == code.lower():
                product.sell(amount)
                return
        print(f"\nProduct '{code}' is not available in the inventory.")
    def show_inventory (self):
        if not self.products:
            print(f"The inventory '{self.name}' has no products")
            return
        print(f"\n--- {self.name} Catalog ---")
        for product in self.products:
            print(product.get_info())
    def search_product (self, code):
        for product in self.products:
            if product.code.lower() == code.lower():
                print(f"\nProduct '{code}' found")
                print(product.get_info())
                return
        print(f"\nProduct '{code}' was not found.")
        
    