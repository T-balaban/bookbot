from stats import count_words
from stats import text_to_character_number
from stats import structurize
import sys

def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(sys.argv[1])
    num_words = count_words(book_content)
    dictionary = text_to_character_number(book_content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in structurize(dictionary):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()