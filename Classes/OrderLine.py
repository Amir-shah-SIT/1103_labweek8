from Classes.Parent.ProductClass import Product

class OrderLine:
    def __init__(self,item:Product,quantity:int) -> None:
        self.__product: Product = item
        self.__quantity: int = quantity 
    
    @property
    def returnitem(self):
        return self.__product
    def showorderline(self):
        print(self.__product.productID)
        print(self.__quantity)
    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity