from Classes.Parent.ProductClass import Products
from Classes.Parent.canBeShippedClass import canBeShippped

class PhysicalProduct(Products,canBeShippped):
    def __init__(self,product_id,name,price,stock,weight):
        super().__init__(product_id,name,price,stock)
        self.__weight = weight
        self._ProductType = "Physical"
    def display_information(self):
        super().display_information()
        print("Product Weight: " + str(self.__weight)+"KG")
    def get_fulfilment_info(self):
        print("product requires physical shipping")
        return "Physical"
    def calculate_shipping_cost(self):
        return 2.5 * self.__weight