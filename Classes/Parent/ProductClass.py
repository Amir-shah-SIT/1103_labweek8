from abc import ABC, abstractmethod
from Classes.SupplierClass import Supplier

class Products(ABC):
    def __init__(self,product_id,name,price,stock,supplier:Supplier):
        self.__supplier : Supplier = supplier
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
