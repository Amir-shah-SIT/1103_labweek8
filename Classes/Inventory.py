from Classes.Parent import ProductClass
class inventory:
    def __init__(self):
        self.__TotalInventory = []

    @property
    def viewinventory(self):
        return self.__TotalInventory
    
    def add_product(self,product):
        self.__TotalInventory.append(product)
        

    def search_product(self,productid):
        targetProduct = next((item for item in self.__TotalInventory if item.productID == productid), None)
        return targetProduct

    def display_all(self):
        for each in self.__TotalInventory:
            each.display_information()


