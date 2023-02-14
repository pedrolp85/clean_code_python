'''
You have decided to play a prank on your programmer friend.

You want to make his code "Lazy". And not in the good way. You want his functions to only run normally 
every nth run, otherwise doing nothing.

To do this, you are going to write a function decorator @lazy(n) where n is the frequency of 'normal' runs. 
For example, if n == 4, then after the first successful run, the next three calls to this function will do nothing, 
and then the 5th run will run normally again. (The first run should always be successful, except for n == -1 which is always lazy).
However, if n is a negative number, then the frequency is inverted (ie. @lazy(-4) means that only every 4th run is lazy, the rest are normal.).
If n == 1, then the function should always be normal, and if n == -1 then the function should always be lazy. n == 0 will never be tested.
Note: When the lazy function 'does nothing', that means it immediately returns None. No lines of the 'normal' function should be run at all.
'''

import functools

def Lazy(argument):

    class _MyDecorator(object):
        def __init__(self, func):
            self.func = func
            self.num_runs = 0

        def __get__(self, obj, type=None):
            return functools.partial(self, obj)

        def __call__(self, *args, **kwargs):
            self.num_runs +=1
            print("ejecution", self.num_runs)
            if argument > 0:
                if ((self.num_runs -1) %  argument) ==0:
                    self.func(*args, **kwargs)
            else:
                print("Nada")
                return None
            

    return _MyDecorator



@Lazy(4)
def test_function_to_decorate() -> None:
    print(f'{"No soy tan vago"}')

for i in range(1,20):
    test_function_to_decorate()