
#kcobela = words we use in the game 
def uses_only(word, letters):
    """Does word use only the allowed letters?"""
    for letter in word:
        if letter not in letters:
            return False
    return True
print(uses_only('cake', 'kcobela'))
print(uses_only('babson', 'kcboela'))

def must_use(word, letter):
    """Does word include the center letter?"""
    for char in word:
        if char == letter:
            return True
    return False 
print(must_use('cake', 'a'))
print(must_use('python', 'a'))

def is_valid(word, letters, required):
    """Find all valid words from a word list."""
    return uses_only(word, letters) and must_use(word, required) and len(word) >=4

def find_words(letters, required):
    file = open("data/words.txt")

    for line in file:
        word = line.strip()
        if is_valid(word, letters, required):
            print(word)
    file.close()


def main():
    """Load words, set up puzzle, print results."""
    print(uses_only("cake", "kcboela"))
    print(uses_only('babson', 'kcboela'))
    print(must_use('cake', 'a'))
    print(must_use('python', 'a'))
    print(is_valid("cake", "kcboela", "a"))
    print(is_valid('babson', 'kcboela', "a"))
    find_words("kcboela", "a")

main()
