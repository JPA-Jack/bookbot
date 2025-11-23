def main():
    a = get_book_text("./books/frankenstein.txt")
    b = split_words(a)
    c = count_ch(a)
    print(f'Found {b} total words')
    print(c)

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import split_words
from stats import count_ch


main()