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

    @property
    def viewinventory(self):
        return self.__TotalInvetory
    
    def add_product(self,product):
        self.__TotalInvetory.append(product)
        

    def search_product(self,productid):
        targetProduct = next((item for item in self.__TotalInvetory if item.productID == productid), None)
        return targetProduct

    def display_all(self):
        for each in self.__TotalInvetory:
            each.display_information()

#Where functions are declared
def add_product(inventoryvariable):
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
    inventoryvariable.add_product(newProduct)

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
    newInventory = inventory()
    try:
        with open('inventory.json', 'r', encoding='utf-8') as file:
            print("Inventory.json found.")
            print("Inventory loaded successfully.")
            loadedinventory = json.load(file)
            for Value in loadedinventory:
                loadProduct = Products(Value["_Products__product_id"],Value["_Products__name"],Value["_Products__price"],Value["_Products__stock"])
                newInventory.add_product(loadProduct)
            return newInventory
    except FileNotFoundError:
        with open("inventory.json", "w+") as file:
            return newInventory

def save_inventory(inventoryvariable):
    tempInventory = []
    for items in inventoryvariable.viewinventory:
        tempInventory.append(items.__dict__)
    with open("inventory.json", "w", encoding="utf-8") as file:
        json.dump(tempInventory, file, indent=4, sort_keys=True)
    print("Inventory save successfully.\n")

def update_stock(inventoryvariable):
        productfound = productSearch(inventoryvariable)
        if productfound != None:
            while True:
                try:
                    newstockInput = int(input("New Stock Quantity: "))
                    productfound.update_stock(newstockInput)
                    return 
                except ValueError:
                    print("Please enter an integer.")

def productSearch(inventoryvariable):
    productSearchInput = input("Enter Product ID: ").upper()
    productFound = inventoryvariable.search_product(productSearchInput)
    if productFound != None:
        print("Product Found.")
        productFound.display_information()
        return productFound
    else:
        print("Product Not Found")

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
            add_product(inventoryObject)
        #update Stock
        case 3:
            update_stock(inventoryObject)
        #Search Product
        case 4:
            productSearch(inventoryObject)
        #save inventory
        case 5:
            print("saving now...")
            save_inventory(inventoryObject)
        #quit
        case 6:
            print("Saving inventory before exiting...")
            save_inventory(inventoryObject)
            print("Thank you for using Inventory Management System.")
            print("Program Terminated.")
            break