#  Hybrid Inheritance in python
# hybrid inheritance- more than 2 inheritance
# Example of Hybrid Inhertance
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass

#  hierarchical Inheritance

class D1(BaseClass):
    pass
class D2(BaseClass):
    pass

class D3(D1):
    pass

