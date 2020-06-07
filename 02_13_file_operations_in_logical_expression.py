import os

def wc (path):
    file = open(path).read()
    file = file.split()
    numberOfWords = len(file)
    return numberOfWords

path = r'c:\Python intermediate\02_13.txt'

#this is standard loop - below I do the same as logical expression

if os.path.isfile(path):
    print('File contains {} words.'.format(wc(path)))


#result of this expression is exactly the same
os.path.isfile(path) and print('File contains {} words.'.format(wc(path)))

