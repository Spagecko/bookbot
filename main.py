from stats import get_book_word_count, count_letters

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    
    return contents 


if __name__ == "__main__":
    myFile = "./books/frankenstein.txt"
    # myContents = get_book_text(myFile)
    # print(myContents)
    myCount = get_book_word_count(myFile)
    myDictLetters = count_letters(myFile)
    print(f"{myCount} words found in the document")
    print(f"{myDictLetters}")