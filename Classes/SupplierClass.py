class Supplier:
    def __init__(self,supplier_id,name,contact_email):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def display_information(self):
        print("Supplier ID: " + self.__supplier_id)
        print ("Supplier Name: " + self.__name)
        print("Contact Email: " + self.__contact_email)
        