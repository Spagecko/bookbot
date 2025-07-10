
def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    
    return contents 

def get_book_word_count(filepath): 
    wordCount = 0 
    with open(filepath) as f:
        strContent = f.read()
        wordsArray = strContent.split()
        wordCount = len(wordsArray)
    
    return wordCount

if __name__ == "__main__":
    myFile = "./books/frankenstein.txt"
    # myContents = get_book_text(myFile)
    # print(myContents)
    myCount = get_book_word_count(myFile)
    print(f"{myCount} words found in the document")