from stats import get_book_word_count, count_letters
import sys

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    
    return contents 


if __name__ == "__main__":
    print(f" count {len(sys.argv)}")
    if(len(sys.argv) != 2 ):
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # myFile = "./books/frankenstein.txt"
    # myContents = get_book_text(myFile)
    # print(myContents)
    myCount = get_book_word_count(sys.argv[1])
    myDictLetters = count_letters(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {myCount} total words")
    print("--------- Character Count -------")
    for l in myDictLetters:
        print(f"{l}: {myDictLetters[l]}")
