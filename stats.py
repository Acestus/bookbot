def get_num_words(text):
    """Count the number of words in the given text."""
    words = text.split()
    return len(words)

def get_char_count(text):
    """Count the frequency of each character in the given text."""
    char_count = {}
    text = text.lower()
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def get_letter_count(text):
    """Count the frequency of only alphabetic characters in the given text."""
    char_count = get_char_count(text)
    only_letters = {k: v for k, v in char_count.items() if k.isalpha()}
    return only_letters