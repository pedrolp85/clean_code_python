
def log(f):
    def new_function(*args,**kwargs):
        print("LLamada a "+str(f))
        print(args)
        print(kwargs)
        return f(*args,**kwargs)
    return new_function
@log
def add(a, b):
    return a + b
print(add(7, 5))

@log
def process(a,b=10,c=1):
    pass
process(3)
process(5,b=5)