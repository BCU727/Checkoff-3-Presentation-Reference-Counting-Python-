import gc

class MyObject:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} destroyed")


a = MyObject("A")
b = MyObject("B")

a.other = b
b.other = a

del a
del b

print("Running garbage collector...")
gc.collect()
