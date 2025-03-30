from stats import wordCount, charCount, sorter
import sys
def get_book_text(path):
    with open(path) as f:
        Words = f.read()
    return Words


def main():
    f = get_book_text(book_path)
    w = wordCount(f)
    
    
    dicto = charCount(f)
    numberedList = sorter(dicto)
    print("BOOKBOT")
    print(f"Found {w} total words")
    for item in numberedList:
        char= item["char"]
        count = item["count"]
        if char.isalpha():
            print(f'{char}: {count}')

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

main()