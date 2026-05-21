def longest(nums):
    nums = set(nums)
    mlength = float('-inf')
    for item in nums:
        length = 0
        if item-1 not in nums:
            current = item
            length = 1
            while(current+1 in nums):
                current += 1
                length += 1
        mlength = max(mlength,length)
    return mlength

print(longest([1,102,2,3,100,100,4]))