from Classes.Inventory import inventory
from Classes.Child.DigitalProductClass import DigitalProduct
from Classes.Child.PhysicalProductClass import PhysicalProduct
from Classes.Parent.ProductClass import Product
from Classes.SupplierClass import Supplier
from Classes.SupllierListClass import SupplierList
import pickle

#Where classes are declared

#Where functions are declared
def add_product(inventoryvariable,suppliervariable):
    chosen_supplier = choose_supplier(suppliervariable)
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
                    tempPhysical_product = PhysicalProduct(productIDinput,productNameinput,productPriceinput,productStockinput,chosen_supplier,product_Weight)
                    inventoryvariable.add_product(tempPhysical_product)
                    break

                except ValueError:
                    print("Enter only a float.")
        case 2:
            while True:
                try:
                    Product_size = int(input("Enter the product size in MB: "))
                    tempDigital_product = DigitalProduct(productIDinput,productNameinput,productPriceinput,productStockinput,chosen_supplier,Product_size)
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
    print("5. Add supplier")
    print("6. Save Inventory")
    print("7. Exit")
    print("------------------------\n")
    while True:
        try:
            mainMenuInput = int(input("Enter Option: "))
            if mainMenuInput > 0 and mainMenuInput < 8:
                return mainMenuInput
            else:
                print("please only enter a number between 1-7.")
        except ValueError:
            print("please only enter a number between 1-7.")

def load_inventory():
    newsupplierlist = SupplierList()
    try:
        with open("data/inventory.pkl", "rb") as file:
            newinventory = pickle.load(file)
            for each in newinventory.viewinventory:
                if len(newsupplierlist.supplier_list) == 0:
                    newsupplierlist.add_supplier(each.supplier)

                for supplier in newsupplierlist.supplier_list:
                    if each.supplier.supplier_name != supplier.supplier_name:
                        newsupplierlist.add_supplier(each.supplier)
            return newinventory, newsupplierlist
    except (EOFError, FileNotFoundError):
        with open("Data/inventory.pkl", "w+") as file:
            return inventory(),SupplierList()

def save_inventory(inventoryvariable):
    with open("data/inventory.pkl", "wb") as file:
        pickle.dump(inventoryvariable, file)
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
    productFound:Products = inventoryvariable.search_product(productSearchInput)
    if productFound != None:
        print("Product Found.")
        show_product_details(productFound)
        return productFound
    else:
        print("Product Not Found")

def add_supplier(supplierlist:SupplierList):
    while True:
        supplier_id = "S" +str(len(supplierlist.supplier_list) + 1).zfill(3)
        supplier_name = input("Supplier Name: ")
        supplier_email = input("Supplier Email: ")
        print("Supplier Name: " + supplier_name)
        print("Supplier Email: " + supplier_email)
        print("Is that correct? ")
        print("1.Yes")
        print("2.No")
        while True:
            try:
                
                match int(input("1 or 2: ")):
                    case 1:
                        new_supplier = Supplier(supplier_id,supplier_name,supplier_email)
                        supplierlist.add_supplier(new_supplier)
                        return new_supplier
                    case 2:
                        break
                    case _:
                        print("Only enter 1 or 2")
            except ValueError:
                print("only enter 1 or 2")

def choose_supplier(supplierlist:SupplierList):
    suppliers = supplierlist.supplier_list
    for index,each in enumerate(suppliers):
        print(str(index+1) + ". "+each.supplier_name)
    print(str(len(suppliers)+1) + ". Create new supplier")
    while True:
        try:
            choose_supplier_input = int(input("Choose an option: "))
            if choose_supplier_input == len(suppliers) + 1:
                newsupplier = add_supplier(supplierlist)
                return newsupplier
            else:
                try:
                    chosensupplier = suppliers[choose_supplier_input - 1]
                    return chosensupplier
                except IndexError:
                    ("that option does not exist")
        except ValueError:
            print("Please enter a number")        

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

inventoryObject, supplierlistobject = load_inventory()
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
            add_product(inventoryObject,supplierlistobject)
        #update Stock
        case 3:
            update_stock(inventoryObject)
        #Search Product
        case 4:
            productSearch(inventoryObject)
        #save inventory
        case 5: 
            add_supplier(supplierlistobject)
        case 6:
            print("saving now...")
            save_inventory(inventoryObject)
        #quit
        case 7:
            print("Saving inventory before exiting...")
            save_inventory(inventoryObject)
            print("Thank you for using Inventory Management System.")
            print("Program Terminated.")
            break