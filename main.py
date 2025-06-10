from stats import get_num_words, get_letter_count

def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        # Count words
        word_count = get_num_words(file_contents)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()
        
        # Count letters
        letter_count = get_letter_count(file_contents)
        # Sort letters by frequency (descending)
        sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        
        for letter, count in sorted_letters:
            print(f"The '{letter}' character was found {count} times")
        
        print("--- End report ---")

main()