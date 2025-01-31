def main(): 
    char_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        for char in file_contents:
            char_count[char] = char_count.get(char, 0) + 1
        only_letters = {k: v for k, v in char_count.items() if k.isalpha()}
        for letter in only_letters:
            print(f"The '{letter}' character was found {only_letters[letter]} times.")

main()