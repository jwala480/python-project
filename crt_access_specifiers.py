#-----Best way to access private variable-----
class A:
    def __init__(self):
        self.__x = 5
        
    def get_x(self):
        return self.__x

class B(A):
    def show(self):
        print(self.get_x())

obj = B()
obj.show()
#-------Best way to access protected variable outside of classes----
class Bank:
    def __init__(self):
        self._balance = 1000

    def get_balance(self):
        return self._balance
obj = Bank()
result = obj.get_balance()
print("Balance (outside classes) = ",result)