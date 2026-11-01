import json
from Inventory import inventory
from ProductClass import PhysicalProduct,DigitalProduct
#Where classes are declared

#Where functions are declared
def add_product(inventoryvariable):
    while True:
        print("Product type?")
        print("1.Physical")
        print("2.Digital")  
        try:
            product_Type = int(input("Choose a Number:"))
            break
        except ValueError:
            print("Invalid input")
    print("Add New Product")
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
    productIDinput = "P" +str(len(inventoryvariable.viewinventory) + 1).zfill(3)

    match product_Type:
        case 1:
            while True:
                try:
                    product_Weight = float(input("Enter the weight of the product in KG: "))
                    tempPhysical_product = PhysicalProduct(productIDinput,productNameinput,productPriceinput,productStockinput,product_Weight)
                    inventoryvariable.add_product(tempPhysical_product)
                    break

                except ValueError:
                    print("Enter only a float.")
        case 2:
            while True:
                try:
                    Product_size = int(input("Enter the product size in MB: "))
                    tempDigital_product = DigitalProduct(productIDinput,productNameinput,productPriceinput,productStockinput,Product_size)
                    inventoryvariable.add_product(tempDigital_product)
                    break
                except ValueError:
                    print("Enter only a integer.")
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
                print(Value["_ProductType"])
                if Value["_ProductType"] == "Physical":
                    loadProduct = PhysicalProduct(Value["_Products__product_id"],Value["_Products__name"],Value["_Products__price"],Value["_Products__stock"],Value["_PhysicalProduct__weight"])
                else:
                    loadProduct = DigitalProduct(Value["_Products__product_id"],Value["_Products__name"],Value["_Products__price"],Value["_Products__stock"],Value["_DigitalProduct__download_size"])
                newInventory.add_product(loadProduct)
            return newInventory
    except (json.JSONDecodeError,FileNotFoundError):
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

inventoryObject = load_inventory()
while True:
    mainMenuBanner()
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