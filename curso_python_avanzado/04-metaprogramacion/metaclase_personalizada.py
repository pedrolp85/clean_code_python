import types

class Mymeta(type):
    def __new__(cls,clase,bases,args):
        nuevos_args={}
        for name, val in args.items():
            if not isinstance(val, types.FunctionType):
                nuevos_args["_"+name]=val
            else:
                nuevos_args[name]=val
        return super().__new__(cls,clase,bases,nuevos_args)

class Test(metaclass=Mymeta):
    data=5
    def metodo():
        print("metodo")

print(Test.__dict__)
obj=Test()
print(obj._data)