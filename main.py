# class Car:
#   name = ""
#   model = ""
#   def Cname(self ):
#     print("Name of car is: " + self.name)
#
# class Model(Car):
#
#   def CModel(self):
#     print("Model is: " + self.model)
#
# #create an object of the subclass
# carname = Model()
# #access superclass attribute and method
# carname.name = "audi"
# carname.model = "2025"
# carname.Cname()
# carname.CModel()


# class VehicleName:
#   name = ""
#   model = ""
#   def VName(self):
#     print("Name of Vehicle is: " , self.name)
#
# class VehicleModel:
#   def VModel(self):
#     print("Vehicle Model is: ", self.model)
#
# class VehicleType(VehicleModel, VehicleName):
#   pass
#
# VehicleName = VehicleType()
# #access superclass attribute and method
# VehicleName.name = "Audi"
# VehicleName.model = 2025
# VehicleName.VName()
# VehicleName.VModel()

# class SuperClass:
#   def super_method(self):
#     print("Super Class Method called")
#
# class DerivedClass1(SuperClass):
#   def derived1_method(self):
#     print("Derived class 1 Method called")
#
# class DerivedClass2(DerivedClass1):
#   def derived2_method(self):
#   def derived2_method(self):
#     print("Derived class 2 Method called")
#
# d2 = DerivedClass2()
# d2.super_method()
# d2.derived1_method()
# d2.derived2_method()


