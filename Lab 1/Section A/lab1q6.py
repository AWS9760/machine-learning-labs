def multiply(*args):
    product = 1
    for num in args:
        product *= num

    return product

nums =[int(x) for x in input("Enter numbers for multiplying: ").split()]

result = multiply(*nums)

print(f"Result: {result}")