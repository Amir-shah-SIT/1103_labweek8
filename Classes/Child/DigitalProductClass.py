from Classes.Parent.ProductClass import Products

class DigitalProduct(Products):
    def __init__(self, product_id, name, price, stock, downloadsize):
        super().__init__(product_id, name, price, stock)
        self.__download_size = downloadsize
        self._ProductType = "Digital"
    def display_information(self):
        super().display_information()
        print("Product Download Size: " + str(self.__download_size)+"MB")
    def get_fulfilment_info(self):
        print("product is delivered digitally")

        return "Digital"