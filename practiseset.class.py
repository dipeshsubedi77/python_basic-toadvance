# create a class programmer for storing information of two programmers working at microsoft
class programmer:
    company = "microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def geinfo(self):
        print("the name of programmer is",self.name,"the name  of product",self.product)
       
dipesh = programmer ("dipesh","apple")
ram = programmer("ram","github")
dipesh.geinfo()
ram.geinfo()