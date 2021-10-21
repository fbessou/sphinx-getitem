import types


class ClassMethod:
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)
        if hasattr(type(self.f), '__get__'):
            return self.f.__get__(cls)
        return MethodType(self.f, cls)


class DemoClass:
    """A special then class"""

#    @ClassMethod
#    def pycls_method(cls):
#        """Using only classmethod"""
#        print("Hello world")

    @classmethod
    def builtincls_method(cls):
        """Using the builtin classmethod"""
        print("Hi there!")
