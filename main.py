from models import Product
from models import Inventory
from exceptions import NotEnoughStockError

def main():
    my_inventory = Inventory("Main Warehouse")
    
    while True:
        print("\n=== MAIN WAREHOUSE ===")
        print("1. Add Product")
        print("2. Show Inventory")
        print("3. Search Product")
        print("4. Sell Product")
        print("5. Exit")
        
        option = input("Select an opcion 1-5: ")
        if option == "1":
            name = input("Enter the product name: ")
            code = input("Enter the product code: ")
            while True:
                try:
                    price = float(input("Enter the product price: "))
                    break
                except ValueError:
                    print("Please enter a valid price (numbers only).")
            while True:
                try:
                    quantity = int(input("Enter the product quantity: "))
                    break
                except ValueError:
                    print("Please enter a valid quantity (numbers only).")
                    
            new_product = Product (name, code, price, quantity)
            my_inventory.add_product(new_product)
                
        elif option == "2":
            my_inventory.show_inventory()
        elif option == "3":
            code = input("Enter the product code: ")
            my_inventory.search_product(code)
        elif option == "4":
            code = input("Enter the product code: ")
            while True:
                try:
                    quantity = int(input("Enter the quantity to sell: "))
                    break
                except ValueError:
                    print("Please enter a valid quantity (numbers only).")
            try:
                my_inventory.sell_product(code, quantity)
            except NotEnoughStockError as error:
                print(error)
            except ValueError as error:
                print(error)
            
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 5.")
        
            
    
if __name__ == "__main__":
    main()