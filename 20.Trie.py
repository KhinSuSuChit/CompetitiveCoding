def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)

if result:
    print("Indices of the two numbers:", result)
    print("The two numbers are:", nums[result[0]], "and", nums[result[1]])
else:
    print("No two numbers sum up to the target.")
