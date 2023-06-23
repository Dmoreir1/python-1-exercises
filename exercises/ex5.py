# Create a Python function named `replace_period` that accepts two inputs:

# - A string that represents a sentence
# - The punctuation character that will replace the period in the sentence

# Usage
# ```python
# sentence = "Test.  This is a test.  Testing."
# sentence2 = replace_period(sentence, "!")
# print(sentence2)
#
# ```
# Ouput:
# ```
# Test!  This is a test!  Testing!

def replace_period(sentence, new_punc):

    sentence = sentence.replace(".", new_punc)
    return sentence

sentence = "Test.  This is a test.  Testing."
sentence2 = replace_period(sentence, "!")
print(sentence2)




# replace_period("Test! This is a test! Testing!", "!")


