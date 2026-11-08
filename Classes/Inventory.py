from Classes.Parent.ProductClass import Product
class inventory:
    def __init__(self):
        self.products: list[Product] = []

    @property
    def viewinventory(self) -> list:
        return self.products
    
    def add_product(self,product:Product)-> None:
        self.products.append(product)
        

    def search_product(self,productid:str)-> Product | None:
        targetProduct = next((item for item in self.__TotalInventory if item.productID == productid), None)
        return targetProduct

    def display_all(self) -> None:
        for each in self.__TotalInventory:
            each.display_information()
            print(each.get_fulfilment_info())

    def remove_product(self,productid:str) -> None:
        self.products.remove(self.search_product(productid))

