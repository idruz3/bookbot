from stats import numbers_of_words
from stats import get_count_words
def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents    

def main():
    filepath = "books/frankenstein.txt"
    get_text = get_book_text(filepath)
    count_words = numbers_of_words(get_text)
    get_chars = get_count_words(get_text)
    print(f"{count_words} words found in the document")
    print(get_chars)


main()