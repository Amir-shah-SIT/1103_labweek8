from Classes.OrderLine import OrderLine
from Classes.Parent.ProductClass import Product
class Order:
    def __init__(self,order_id:str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
    
    def add_order_line(self,product:Product, quantity:int) -> None:
        order_line = OrderLine(product,quantity)
        self.order_lines.append(order_line)
    
    def calculate_total(self) -> int:
        total = 0
        for each in self.order_lines:
            total += each.calculate_subtotal()
        
        return total
    

