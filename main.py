import json
#Where classes are declared
class Products:
    def __init__(self,product_id,name,price,stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    @property
    def productID(self):
        return self.__product_id
    
    def update_stock(self,quantity):
        self.__stock = quantity

    def display_information(self):
        print("----------------------------------------")
        print("Product ID:" + self.__product_id)
        print("Product Name: " + self.__name)
        print("Product Price: "+ str(self.__price))
        print("Prodcut Stock: " + str(self.__stock))

class inventory:
    def __init__(self):
        self.__TotalInvetory = []

    def add_product(self,product):
        self.__TotalInvetory.append(product)
        

    def search_product(self,productid):
        targetProduct = next((item for item in self.__TotalInvetory if item.produdtID == productid), None)
        if targetProduct != None :
            return targetProduct
        else:
            print("No product exists")

    def display_all(self):
        for each in self.__TotalInvetory:
            each.display_information()

#Where functions are declared
def add_product():
    print("Add New Product")
    productIDinput = input("Product ID:").upper()
    productNameinput = input("Product Name: ")
    while True:
        try:
            productPriceinput = float(input("Price: "))
            break
        except ValueError:
            print("Enter only a number.")
    while True:
        try:
            productStockinput = int(input("Stock Quantity: "))
            break
        except ValueError:
            print("Enter only a integer.")
    newProduct = Products(productIDinput,productNameinput,productPriceinput,productStockinput)
    inventory[productIDinput] = newProduct

    return

def mainMenuBanner():
    print("=========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=========================================\n")
        
def mainMenuOptions():
    print("\n------------------------")
    print("1. Display All Products")
    print("2. Add Products")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------\n")
    while True:
        try:
            mainMenuInput = int(input("Enter Option: "))
            if mainMenuInput > 0 and mainMenuInput < 7:
                return mainMenuInput
            else:
                print("please only enter a number between 1-6.")
        except ValueError:
            print("please only enter a number between 1-6.")

def load_inventory():
    try:
        with open('inventory.json', 'r', encoding='utf-8') as file:
            print("Inventory.json found.")
            print("Inventory loaded successfully.")
            loadedinventory = json.load(file)
            for Value in load_inventory:
                loadProduct = Products(Value["productID"],Value["productName"],Value["productPrice"],Value["productStock"])
                newInventory = inventory.add_product(loadProduct)
            return newInventory
    except FileNotFoundError:
        with open("inventoryList.txt", "w+") as file:
            json.dump(inventory, file, indent=4)
            return inventory()

def save_inventory():
    with open("inventory.json", "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4, sort_keys=True)
    print("Inventory save successfully.\n")

def update_stock(inventory):
        updateStockinput = input("Enter Product ID: ").upper()
        for each in inventory:
            each[]
            print("Product Found.")
            print("Name: " + inventory[updateStockinput]["productName"])
            print("Current Stock: "+ str(inventory[updateStockinput]["productStock"]))
            try:
                newstockInput = int(input("New Stock Quantity: "))
                inventory[updateStockinput]["productStock"] = newstockInput
                return 
            except ValueError:
                print("Please enter an integer.")
        else:
            print("Product not found.")


mainMenuBanner()
inventoryObject = load_inventory()
while True:
    menuInput = mainMenuOptions()
    print("\n")
    match menuInput:
        #Display product
        case 1:
            inventoryObject.display_all()
            
        #Add Products
        case 2:
            add_product()
        #update Stock
        case 3:
            update_stock()
        #Search Product
        case 4:
            search_product()
        #save inventory
        case 5:
            print("saving now...")
            save_inventory()
        #quit
        case 6:
            print("Saving inventory before exiting...")
            save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program Terminated.")
            break