from collections import abc

def double(x):
    return x * 2


def annotated_double(x: abc.Sequence):
    return x * 2


print(double(["a", "b", "c"]))
print(double(2))
print(double(("a", "b", "c")))
#print(double({"a": "b"}))

print(annotated_double(["a", "b", "c", "d"]))
print(annotated_double(2))
print(annotated_double(("a", "b", "c", "d")))
print(annotated_double({"a": "b"}))

