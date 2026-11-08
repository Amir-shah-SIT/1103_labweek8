from Classes.Inventory import inventory
from Classes.Child.DigitalProductClass import DigitalProduct
from Classes.Child.PhysicalProductClass import PhysicalProduct
from Classes.Parent.ProductClass import Product
from Classes.SupplierClass import Supplier
from Classes.SupllierListClass import SupplierList
from Classes.Order import Order
from Classes.OrderLine import OrderLine


newsupplier1 = Supplier("S001","Singtel","singtel@singnet.sg")
physicalproduct1 = PhysicalProduct("P001","basketball",27,66,newsupplier1,0.6)
digitalproduct1 = DigitalProduct("P002","windows",100,99,newsupplier1,500)

print("test 1----------------------------------------")
physicalproduct1.supplier.display_information()
digitalproduct1.supplier.display_information()


print("test2----------------------------------------")
newinventory1 = inventory()
newinventory1.add_product(physicalproduct1)
newinventory1.display_all()
print("before remove")
newinventory1.remove_product("P001")
print("after remove")
newinventory1.display_all()
physicalproduct1.display_information()


print("test3---------------------------------------")
neworder1 = Order("O001")
neworder1.add_order_line(digitalproduct1,50)
neworder1.add_order_line(physicalproduct1, 20)
neworder1.display_all()
print(neworder1.calculate_total())
neworder2 = Order("O002")
neworder1.remove_order(digitalproduct1)
print("displaying order 1 =========================")
neworder1.display_all()
print("displaying order 2 =========================")

neworder2.add_order_line(digitalproduct1,90)
neworder2.add_order_line(physicalproduct1,21)
neworder2.display_all()

print("test3 ==============================================")

newinventory2 = inventory()
newinventory2.add_product(physicalproduct1)
newinventory2.add_product(digitalproduct1)
