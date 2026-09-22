def swap(a, b):
    a, b = b, a
    print("After swapping: ")
    print(f"a = {a}, b = {b}")
    
a = 4
b = 8
print("Before swapping: ")
print(f"a = {a}, b = {b}")
swap(a, b)