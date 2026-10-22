class Products:
    def __init__(self,product_id,name,price,stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self,quantity):
        self.__stock = quantity

    def display_information(self):
        print("----------------------------------------")
        print("Product ID:" + self.__product_id)
        print("Product Name: " + self.__name)
        print("Product Price: "+ str(self.__price))
        print("Prodcut Stock: " + str(self.__stock))

