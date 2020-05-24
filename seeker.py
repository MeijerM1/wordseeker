#!/bin/python 
import sys
import time

# Read command line parameters
try:
    gridsize  = int(sys.argv[1])
    word      = sys.argv[2]
    data_file = open(sys.argv[3], "r")
except:
    sys.exit("Error: could not open file for reading \nUsage: ws <gridSize> <word> <gridFile>")

lines = data_file.readlines()
data_file.close()

# Validate that gridFile matches the suppied parameters
if len(lines) != gridsize:
    sys.exit("Error: provided grid size does not match grid file")
    
for line in lines:
    line = line.rstrip()
    if len(line) != int(gridsize):
        sys.exit("Error: provided grid size does not match grid file")


#
#           7 0 1
#           6 S 2
#           5 4 3

# S : define by X,Y  characters in the list (0,0) is upperleft

def checkChar (char, x, y):
    """ Check a given character at the specified position x,y"""
    if x < 0 or x >= gridsize or y < 0 or y >= gridsize:
       return False

    return lines[y][x] == char

def checkWord (word, x, y, incX, incY):
    """ Check a given position in the list for a supplied word """

    # Check each character of the string
    for c in word:
        if not checkChar(c, x, y):
            return False
        x += incX
        y += incY

    return True

def checkOrientations (word, x, y):
    """ Check a given word in all 8 orientations on a given position"""

    r = checkWord (word,x ,y, 0, 1)
    r = r or checkWord (word, x ,y, 1, 1)
    r = r or checkWord (word, x ,y, 1, 0)
    r = r or checkWord (word, x ,y, 1, -1)
    r = r or checkWord (word, x ,y, 0, -1)
    r = r or checkWord (word, x ,y, -1, -1)
    r = r or checkWord (word, x ,y, -1, 0)
    r = r or checkWord (word, x ,y, -1, 1)
    return r

def findWord (word):
    result = False
    for x in range(gridsize):
        for y in range(gridsize):
            result = result or checkOrientations(word, x, y)
            if result: 
                return result

    return False

iterations = 100000

start = time.time()
for x in range(iterations):
    findWord(word)

end = time.time()


print(F'Searching took: {(end - start) / iterations}')