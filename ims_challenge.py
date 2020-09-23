

class Product():
    # def __init__(self,name):
    #     self.name=name
    def __init__(self,name,count):
        self.name=name
        self.count=count


class Warehouse():
    def __init__(self,location):
        self.location=location
        # self.products = []#if you want to make it a dictionary use .get() to check wether the product already exists in dictionary
        self.products={}
    def add_product(self,product_name,count):
        # for i in range(0,count):
            # self.products.append(Product(product_name))
        if self.products.get(product_name):
            self.products[product_name].count+=count
        else:
            self.products[product_name]=Product(product_name,count)
    def remove_product(self,product_name,count):
        # for i in range(0,count):
        #     for idx, product in enumerate(self.products):
        #         if product.name==product_name:
        #             self.products.pop(idx)
        #             break
        self.products[product_name].count-=count
            

class Store():
    def __init__(self,name):
        self.name = name
        # self.warehouses = []
        self.warehouses = {}
    def add_warehouse(self,location):
        self.warehouses[location]=Warehouse(location)
    def add_product(product_name,count,location):
        self.warehouses[location].add_product(product_name,count)
    def remove_product(product_name,count):
        self.warehouses[location].remove_product(product_name,count)

    def check_product_availability(self,product_name):
        count = 0
        for warehouse in self.warehouses.values():
            # for product in warehouse.products:
            #     if product.name==product_name:
            #         count+=1
            count+=warehouse.products[product_name].count
        return count


my_store = Store('mystore')
my_store.add_warehouse('damansara')

my_store.warehouses['damansara'].add_product('NikeAirMax',10)
my_store.warehouses['damansara'].remove_product('NikeAirMax',2)
# print(my_store.warehouses['damansara'].products['NikeAirMax'].count)
print(my_store.check_product_availability('NikeAirMax'))