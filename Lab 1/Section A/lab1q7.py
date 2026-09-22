def char_frequency(s):
    return {ch: s.count(ch) for ch in set(s)}

print(f"Character Frequency: {char_frequency('Hello Machine Learning')}")