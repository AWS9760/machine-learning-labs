def fibonacci(n):
    seq = []
    a, b = 0, 1
    
    for i in range(n):
        seq.append(a)
        a, b = b, a + b
        
    return seq

n = int(input("Enter the number of fibonacci sequence: "))
print(fibonacci(n))