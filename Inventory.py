from ProductClass import Products
class inventory():
    def __init__(self):
        self.__TotalInvetory = []

    def add_product(self,product):
        self.__TotalInvetory.append(product)
        

    def search_produdct(self,product):
        if product in self.__TotalInvetory:
            product.display_information()
        else:
            print("No product exists")

    def display_all(self):
        for each in self.__TotalInvetory:
            each.display_information()

item1 = Products("P001","Baseball",99,50)
item2 = Products("P002","Basketball",99,67)


maininventory= inventory()

maininventory.add_product(item1)
maininventory.add_product(item2)
maininventory.search_produdct(item1)
maininventory.search_produdct("test")

maininventory.display_all()


