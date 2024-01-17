from typing import NoReturn

# from typing import Never (Python 3.11+


def stop() -> NoReturn:
    raise Exception("no way")


def unreachable_code() -> None:
    stop()
    print("Ok!")


def never_call_me(arg: NoReturn) -> None:
    pass


def int_or_str(arg: int | str) -> None:
    never_call_me(arg)  # type checker error
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _:
            never_call_me(arg)  # OK, arg is of type Never
