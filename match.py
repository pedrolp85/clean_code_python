
our_string : str = "Hola"

match our_string.lower():
    
    case "hola":
        print("ola k ase")
    case _:
        print("nada k aser")

myvar = 'wtf'
inp = 'Foo'
match inp:
    case myvar if myvar :=inp.lower():
        print("esto siempre es success!")
    case _:
        print("esto nunca da error!")