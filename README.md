# Reference Counting in Python

**COMP 211 – Checkoff 3**

A look into how CPython manages memory using reference counting, automatically tracks references to objects, and deallocates objects when they are no longer being used.

## Overview

Python uses automatic memory management to handle the allocation and deallocation of objects. One of the primary techniques used by CPython is reference counting.

Reference counting works by keeping track of how many references point to an object. When an object's reference count reaches zero, CPython can deallocate that object and reclaim its memory.

This project looks into how reference counting works, how CPython implements it, and some of its limitations, including the problem of circular references.

## Key Concepts

### 1. How Reference Counting Works

In Python, multiple variables can reference the same object in memory.

For example:

a = [1, 2, 3]
b = a

Both `a` and `b` reference the same list object. CPython tracks these references using an internal reference count.

- Creating another reference increases the reference count.
- Removing a reference decreases the reference count.
- When the count reaches zero, the object can be deallocated.

The `sys.getrefcount()` function can be used to inspect an object's reference count.

**Note**: `sys.getrefcount()` temporarily creates an additional reference to the object, so its returned value is typically one higher than the count you might expect.

### 2. CPython's Implementation

CPython maintains reference-count information as part of its internal object representation.

Two important operations are:

- `Py_INCREF()`: Increments an object's reference count.
- `Py_DECREF()`: Decrements an object's reference count.

When a reference count reaches zero, CPython proceeds with the object's deallocation process.

### 3. Object Deallocation

When an object no longer has any references pointing to it, CPython can deallocate it.

For example:


a = [1, 2, 3]
b = a

del a  
del b 

The `del` statement removes a reference, not necessarily the object itself.

### 4. Circular References

One limitation of reference counting is that it cannot independently handle circular references.

A circular reference occurs when two or more objects reference one another.

a = []
b = []

a.append(b)
b.append(a)

del a
del b

Even after deleting both variables, the objects still reference each other. Their reference counts therefore do not reach zero.

CPython addresses this problem through its cyclic garbage collector, which can identify and reclaim unreachable groups of objects that reference one another.

## Experiments

This project includes three Python experiments demonstrating different aspects of reference counting.

`reference_counting.py` Uses `sys.getrefcount()` to observe how references affect an object's reference count.
`object_destruction.py` Demonstrates how objects are deallocated after their final reference is removed.
`circular_references.py` Demonstrates circular references and how Python's cyclic garbage collector handles them.

To test the expiriments, copy and paste the code into this online code compiler: https://www.programiz.com/python-programming/online-compiler/

## Python vs. C Memory Management

Reference counting provides an interesting comparison between Python and C.

Python (CPython)

Memory allocation: Automatically managed. 
Memory deallocation: Reference counting and garbage collection. 
Reference tracking: Handled internally by CPython. 
Memory management: Mostly manual.

C

Memory allocation: Typically managed with `malloc()` or other allocation functions.
Memory deallocation: Programmer calls `free()` for allocated memory.
Reference tracking: Programmer manages pointers.
Memory management: Mostly manual.

In C, programmers are responsible for releasing dynamically allocated memory. Forgetting to free memory can result in memory leaks, while incorrectly freeing memory can cause errors such as double frees or use-after-free.

CPython automates much of this process through reference counting and garbage collection, reducing the amount of manual memory management required.

## Key Takeaways

Through this exploration, I learned:

1. CPython tracks references to objects to determine when they are no longer needed.
2. Multiple variables can reference the same object without creating separate copies.
3. When an object's reference count reaches zero, CPython can deallocate it.
4. Reference counting alone cannot reclaim unreachable circular references.
5. CPython uses cyclic garbage collection alongside reference counting to handle these situations.
6. Python simplifies memory management compared to C, but memory management still has limitations.

One of the most interesting discoveries was that deleting a variable does not necessarily destroy the object it references. An object remains as long as references to it still exist.

**Topic:** Reference Counting (Python)  
**Course:** COMP 211  
**Language:** Python  
**Implementation:** CPython
