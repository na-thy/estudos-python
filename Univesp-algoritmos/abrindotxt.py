def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList),len(content)

n_words, n_chars = readFile('texto.txt')

print(n_words)
print(n_chars)

