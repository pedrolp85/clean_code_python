import functools


class MyDecorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.allowed = True

    def __call__(self, *args, **kwargs):
        if self.allowed:
            self.func()
        else:
            print("shhh")


@MyDecorator
def shout():
    print(f'{"HOLAAAAA!!!"}')


shout()
