import sys

a = [10, 20, 30]
b = a

print(sys.getrefcount(a))

del a

print(sys.getrefcount(b))

del b
