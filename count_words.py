def count_words(filename, word):
    count = 0
    with open(filename, "r") as file:
        content = file.read()
    for i in content.split():
        if i == word:
            count += 1
    return count

print(count_words("count_words_test.txt", "the"))

