def get_book_word_count (filepath): 
    wordCount = 0 
    with open(filepath) as f:
        strContent = f.read()
        wordsArray = strContent.split()
        wordCount = len(wordsArray)
    
    return wordCount

def count_letters(filepath):
    charDict = {}
    with open(filepath) as f:
        strContent = f.read()
        strLowerContent = strContent.lower()
        for c in strLowerContent:
            if(charDict.__contains__(c) != True):
                charDict.update({c:1})
            else:
                currentCount = charDict[c]
                currentCount = currentCount + 1
                charDict.update({c:currentCount})
    
    return charDict
    
