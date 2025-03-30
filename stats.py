def wordCount(x):
    words = x.split()
    return len(words)

def charCount(x):
    countDict = {}
    count = 0
    for letter in x:
        lletter = letter.lower()
        if lletter in countDict:
            countDict[lletter] +=1
        else:
            countDict[lletter] = 1
    return countDict

def sorter(x):
    charList = []
    for char, count in x.items():
        charList.append({"char": char, "count": count})

    def sort_on(x):
        return x["count"]
    
    charList.sort(reverse=True, key=sort_on)
    return charList