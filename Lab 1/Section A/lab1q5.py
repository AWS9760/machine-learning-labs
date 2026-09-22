def count_chars(s):
    vowels = consonents = digits = spaces = 0
    for ch in s:
        low = ch.lower()
        if low in "aeiou":
            vowels += 1
        elif low.isalpha():
            consonents += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1  
    
    return vowels, consonents, digits, spaces

v, c, d, sp = count_chars("My name is Abdul Wali")
print(f"Vowels = {v}, Consonants = {c}, Digit = {d}, Spaces = {sp}")