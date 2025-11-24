import sys

def main():
    a = get_book_text(sys.argv[1])
    b = split_words(a)
    c = count_ch(a)
    print(f'Found {b} total words')
    list1 = split_dict (c)
    list1.sort(reverse=True, key=sort_on)
    for i in list1:
        print(f'{i["name"]}: {i["num"]}')


def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import split_words
from stats import count_ch
from stats import split_dict
from stats import sort_on
import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys,exit(1)
else:
    main()