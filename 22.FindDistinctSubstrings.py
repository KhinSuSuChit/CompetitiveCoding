def distinct_substrings(s):
    n = len(s)
    substrings = set()
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.add(s[i:j])
    return substrings

# Example usage:
input_string = "abc"
distinct = distinct_substrings(input_string)
print("Distinct substrings in '{}' are:".format(input_string))
print(distinct)
