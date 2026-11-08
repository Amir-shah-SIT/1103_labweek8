from Classes.Parent.ProductClass import Product
from Classes.Parent.canBeShippedClass import canBeShippped

class PhysicalProduct(Product,canBeShippped):
    def __init__(self,product_id,name,price,stock,supplier,weight):
        super().__init__(product_id,name,price,stock,supplier)
        self.__weight = weight
        self._ProductType = "Physical"
    def display_information(self) -> None:
        super().display_information()
        print("Product Weight: " + str(self.__weight)+"KG")
    def get_fulfilment_info(self):
        print("product requires physical shipping")
        return "Physical"
    def calculate_shipping_cost(self) -> int:
        return 2.5 * self.__weight