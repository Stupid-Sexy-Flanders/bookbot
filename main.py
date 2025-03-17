import sys
from stats import get_num_words, get_characters, sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    list = sorted_list(get_characters(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list:
        print(item)
    print("============= END ===============")

main()
