# Create a Python function named `slice_it` that accepts an array `strings` and returns the first two letters of every
# word.
#
# [String slicing](https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3)
#
# Usage:
# ```python
# array = ["this", "is", "another", "test"]
# r = slice_it(array)
# print(r)
# ```
#
# Ouput:
# ```
# th is an te
# ```
def slice_it(array):
    result = []

    for word in array:
        if len(word) >= 2:
            result.append(word[:2])

        else:
            result.append(word)
    return result

array = ["this", "is", "another", "test"]
result = slice_it(array)

print(result)

# for element in array
#     newString = newString + element[:2]