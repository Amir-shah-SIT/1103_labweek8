from Classes.SupplierClass import Supplier

class SupplierList:
    def __init__(self):
        self.__supplierList = []

    def add_supplier(self,supplier):
        self.__supplierList.append(supplier)

    @property
    def supplier_list(self):
        return self.__supplierList