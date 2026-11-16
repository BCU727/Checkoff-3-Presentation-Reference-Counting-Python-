import sys

my_list = [1, 2, 3]

print("After creation:", sys.getrefcount(my_list))

second_reference = my_list

print("After second reference:", sys.getrefcount(my_list))

third_reference = my_list

print("After third reference:", sys.getrefcount(my_list))

del second_reference

print("After deleting second reference:", sys.getrefcount(my_list))

del third_reference

print("After deleting third reference:", sys.getrefcount(my_list))
