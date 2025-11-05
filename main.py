from stats import count_words
from stats import text_to_character_number
from stats import structurize
def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_content)
    dictionary = text_to_character_number(book_content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in structurize(dictionary):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()