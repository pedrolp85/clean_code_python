# https://www.programiz.com/python-programming/generator
# A simple generator function
def my_gen():
    n = 1
    print("This is printed first")
    # Generator function contains yield statements
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed at last")
    yield n


generator = my_gen()
print(generator)  # we can see that like an array

first_value = next(generator)
print(first_value)
print(generator)


second_value = next(generator)
print(second_value)
print(generator)


third_value = next(generator)
print(third_value)
print(generator)

# print("We have problems!")
# fourth_value = next(generator)


for v in my_gen():
    print(f"In the loop {v}")


def pow(n, m):
    print("Calculate the pow!")
    return n**m


# Initialize the list
my_list = range(10)

print("We will create the list!")
# square each term using list comprehension
list_ = [pow(x, 2) for x in my_list]
print(list_)


print("We will create the generator!")
# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (pow(x, 2) for x in my_list)
print(generator)

print("we will iterate over the list")
for el in list_:
    print(el)

print("we will iterate over the generator")
for g in generator:
    print(g)


class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2**self.n
        self.n += 1
        return result


def all_even():
    n = 0
    while True:
        yield n
        n += 2


evens = all_even()
for _ in range(10000):
    print(next(evens))


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num**2


print(sum(square(fibonacci_numbers(10))))


class Greating:
    def greating(name):
        print(f"Hello {name}")


class RudeGreating(Greating):
    def greating(_):
        print(f'{"HELLO!"}')
