from stats import word_count
from stats import char_count
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def final_report(book_file, num_words, sorted_char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_file = sys.argv[1]
    book_text = get_book_text(book_file)
    num_words = word_count(book_text)
    dictionary = char_count(book_text)
    sorted_char_count = sort_dict(dictionary)
    final_report(book_file, num_words, sorted_char_count)

main() 