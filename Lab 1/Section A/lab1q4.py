def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

arr = [1,1,2,3,4,4,5,6,7,8,8,9,10]
print(remove_duplicates(arr))