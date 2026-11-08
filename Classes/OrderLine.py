from Classes.Parent.ProductClass import Product

class OrderLine:
    def __init__(self,item:Product,quantity:int) -> None:
        self.__product: Product = item
        self.__quantity: int = quantity 
    
    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity