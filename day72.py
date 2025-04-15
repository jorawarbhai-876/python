# Super keyword
class Parentclass:
    def parent_method(self):
        print("this is the parent method1.")

class ChildClass(Parentclass):
    def parent_method(self):
        print("harry")
        super().parent_method()
    def child_method(self):
        print("this is the child method2")

    super().parent_method()
    child_object = ChildClass()
    child_object.child_method()
    child_object.parent_method()