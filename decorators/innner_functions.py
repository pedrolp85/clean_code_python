def parent_function():
    print("Printing from the parent() function")

    def inner_function_one() -> None:
        print("Printing from the first inner function")

    def inner_function_two() -> None:
        print("Printing from the second inner function")

    inner_function_two()
    inner_function_one()


parent_function()
print("\n")
try:
    inner_function_one()
except NameError:
    print(f'{"NameError occurred. The function is not defined."}')
