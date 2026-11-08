from abc import ABC, abstractmethod
from Classes.SupplierClass import Supplier

class Product(ABC):
    def __init__(self,product_id:str,name:str,price:float,stock:int,supplier:Supplier):
        self.__supplier : Supplier = supplier
        self.__product_id : str= product_id
        self.__name :str = name
        self.__price :float= price
        self.__stock :int = stock
    
    @property
    def productID(self):
        return self.__product_id
    @property
    def supplier(self):
        return self.__supplier
    @property
    def price(self):
        return self.__price
    def update_stock(self,quantity):
        self.__stock = quantity

    def display_information(self) -> None:
        print("----------------------------------------")
        print("Product ID:" + self.__product_id)
        print("Product Name: " + self.__name)
        print("Product Price: "+ str(self.__price))
        print("Product Stock: " + str(self.__stock))
        print("Supplier: " + self.__supplier.supplier_name)
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass
    
