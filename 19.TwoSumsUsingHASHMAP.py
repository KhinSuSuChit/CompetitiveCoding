def two_sum(nums, target):
    # Create a dictionary to store the numbers we have seen so far and their indices
    num_map = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement of the current number (target - num)
        complement = target - num

        # If the complement exists in the dictionary, return the pair of indices
        if complement in num_map:
            return [num_map[complement], i]

        # Otherwise, store the current number with its index in the dictionary
        num_map[num] = i

    # If no solution is found, return None
    return None


# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices of the two numbers that add up to target:", result)
