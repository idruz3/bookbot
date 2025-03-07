from stats import numbers_of_words
from stats import get_count_words
from stats import get_sorted
import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = numbers_of_words(book_text)
    char_counts = get_count_words(book_text)
    sorted_chars = get_sorted(char_counts)
    
    print(f"Found {word_count} total words")
    for char in sorted_chars:
        print(f"{char}: {sorted_chars[char]}")

if __name__ == "__main__":
    main()