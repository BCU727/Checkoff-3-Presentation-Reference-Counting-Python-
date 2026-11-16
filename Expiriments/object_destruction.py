class MyObject:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")


a = MyObject("Object A")
b = a

print("Deleting a...")
del a

print("Deleting b...")
del b

print("Program finished")
