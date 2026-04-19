#--------------Access Specifiers------------
#-------Public Access Specifier---------
class Student:
    def __init__(self):
        self.name = "Ram"
    def display(self):
        print("Name:",self.name)
obj = Student()
obj.display()
print("Name:",obj.name)
#-----Private Access Specifier-------
class Parent:
    def __init__(self):
        self._money = 1000
class Child(Parent):
    def display(self):
        print("Money from parent:",self._money)
obj = Child()
obj.display()
# Access outside but discouraged
print("Money outside classes:",obj._money)
#--------Private Access specifier-------
class Employee:
    def __init__(self):
        self.__salary = 50000  # Private variable

    def show(self):
        print("Salary:", self.__salary)

obj = Employee()
obj.show()

# This will cause error:
#print(obj.__salary)
# By Access this private access secifier using Name Mangling
print("Salary (outside class) = ",obj._Employee__salary)
