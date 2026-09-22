def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    
    return cleaned == cleaned[::-1]

print(f"Is Race Car a palindrome: {is_palindrome("Race Car")}")