
class employee:
   def __init__(self,name) :
    self.name = name
   def getsalary(self):
     print("the name of emplyee is",self.name)

p1 = employee("dipesh")
print(p1.getsalary())
    