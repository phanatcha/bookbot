import sys
from stats import get_num_words, count_letter, formatted_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
            
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = count_letter(text)
    char_count = formatted_dict(letter_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in char_count:
        char = entry["char"]
        if char.isalpha(): 
            print(f"{char}: {entry['num']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
