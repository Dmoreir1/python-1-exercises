
def count_words():
    user_input = input("Type sentence here:")

    words = user_input.split()

    word_count = len(words)

    return word_count


num_words = count_words()

print("Words total:", num_words)

