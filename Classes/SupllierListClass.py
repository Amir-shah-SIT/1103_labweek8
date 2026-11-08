from Classes.SupplierClass import Supplier

class SupplierList:
    def __init__(self):
        self.__supplierList: list[Supplier] = []

    def add_supplier(self,supplier:Supplier):
        self.__supplierList.append(supplier)

    @property
    def supplier_list(self) -> list:
        return self.__supplierList