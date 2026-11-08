from Classes.Parent.ProductClass import Product
from Classes.SupplierClass import Supplier
class DigitalProduct(Product):
    def __init__(self, product_id:str, name:str, price:float, stock:int, supplier:Supplier,downloadsize:int):
        super().__init__(product_id, name, price, stock,supplier)
        self.__download_size:int = downloadsize
        self._ProductType = "Digital"
    def display_information(self) -> None:
        super().display_information()
        print("Product Download Size: " + str(self.__download_size)+"MB")
    def get_fulfilment_info(self) -> str:
        print("product is delivered digitally")

        return "Digital"