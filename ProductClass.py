from abc import ABC, abstractmethod

class Products(ABC):
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
        print("Product Stock: " + str(self.__stock))
    
    @abstractmethod
    def get_fulfilment_info():
        pass

class canBeShippped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Products,canBeShippped):
    def __init__(self,product_id,name,price,stock,weight):
        super().__init__(product_id,name,price,stock)
        self.__weight = weight
    def display_information(self):
        super().display_information()
        print("Product Weight: " + str(self.__weight)+"KG")
    def get_fulfilment_info(self):
        print("product requires physical shipping")
        return "Physical"
    def calculate_shipping_cost(self):
        return 2.5 * self.__weight
        
        
class DigitalProduct(Products):
    def __init__(self, product_id, name, price, stock, downloadsize):
        super().__init__(product_id, name, price, stock)
        self.__download_size = downloadsize

    def display_information(self):
        super().display_information()
        print("Product Download Size: " + str(self.__download_size)+"MB")
    def get_fulfilment_info(self):
        print("product is delivered digitally")
        return "Digital"

