"""

def shout(word="yes"):
    return word.capitalize() + "!"


print(shout("mi nombre es pedro"))

print(shout)

scream = shout

print(scream("mi nombre es pedro"))

del shout
try:
    print(shout("mi nombre es pedro"))
except NameError as e:
    print(e)

print(scream("mi nombre es pedro"))


########################################


def talk():
    # You can define a function on the fly in `talk` ...
    def whisper(word="yes"):
        return word.lower() + "..."

    print(whisper())


# You call `talk`, that defines `whisper` EVERY TIME you call it, then
# `whisper` is called in `talk`.
talk()
# outputs:
# "yes..."

# But `whisper` DOES NOT EXIST outside `talk`:

try:
    print(whisper())
except NameError as e:
    print(e)
    # outputs : "name 'whisper' is not defined"*

########################################################


def getTalk(kind="shout"):

    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize() + "!"

    def whisper(word="yes"):
        return word.lower() + "..."

    # Then we return one of them
    if kind == "shout":
        # We don’t use '()'. We are not calling the function;
        # instead, we’re returning the function object
        return shout
    else:
        return whisper


# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()

# You can see that `talk` is here a function object:
print(talk)
# outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
print(talk())
# outputs : Yes!

# And you can even use it directly if you feel wild:
print(getTalk("whisper")())

###################


def doSomethingBefore(func):
    print("I do something before then I call the function you gave me")
    print(func())


doSomethingBefore(scream)

################################################################


# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original
        # function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original
        # function is called
        print("After the function runs")

    # At this point, `a_function_to_decorate` HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before
    # and after. It’s ready to use!
    return the_wrapper_around_the_original_function


# Now imagine you create a function you don’t want to ever touch again.
def a_stand_alone_function():
    print("I am a stand alone function, don’t you dare modify me")


a_stand_alone_function()
# outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in
# any code you want and return you a new function ready to be used:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
# outputs:
# Before the function runs
# I am a stand alone function, don't you dare modify me
# After the function runs

##################################################################


@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")


another_stand_alone_function()

##################################################################


def bread(func):
    def wrapper(food):
        print(r"</""" r"""\>")
        func(food)
        print(r"<\______/>")

    return wrapper


def ingredients(func):
    def wrapper(food):
        print("#tomatoes#")
        func(food)
        print("~salad~")

    return wrapper


@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)


sandwich("--tofu--")

#######################################################################


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("I got args! Look:", arg1, arg2)
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


# Since when you are calling the function returned by the decorator, you are
# calling the wrapper, passing arguments to the wrapper will let it pass them to
# the decorated function


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name is", first_name, last_name)


print_full_name("Peter", "Venkman")

##############################################################


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # very friendly, decrease age even more :-)
        return method_to_decorate(self, lie)

    return wrapper


class Lucy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am {}, what did you think?".format(self.age + lie))


l = Lucy()
l.sayYourAge(-3)


#############################################################


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Do I have args?:")
        print(args)
        print(kwargs)
        # Then you unpack the arguments, here *args, **kwargs
        # If you are not familiar with unpacking, check:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")


function_with_no_argument()
# outputs
# Do I have args?:
# ()
# {}
# Python is cool, no argument here.


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)
# outputs
# Do I have args?:
# (1, 2, 3)
# {}
# 1 2 3


@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print("Do {}, {} and {} like platypus? {}".format(a, b, c, platypus))


function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")
# outputs
# Do I have args ? :
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# Do Bill, Linus and Steve like platypus? Indeed!


class Mary:
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):  # You can now add a default value
        print("I am {}, what did you think?".format(self.age + lie))


m = Mary()
m.sayYourAge()
# outputs
# Do I have args?:
# (<__main__.Mary object at 0xb7d303ac>,)
# {}
# I am 28, what did you think?
"""
