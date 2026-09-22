def odd_nums(nums):
    odds = list(filter(lambda x: x % 2 != 0, nums))
    print(f"Odd Numbers: {odds}")
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums(nums)