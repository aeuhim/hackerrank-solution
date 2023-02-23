# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys

def generateResult(line):
    line_splitted = line.split(";")
    operation = line_splitted[0]
    
    if operation == 'S':
        word = line_splitted[2]
        return performSplit(word)
    
    if operation == 'C':
        identifier_type = line_splitted[1]
        words = line_splitted[2]
        return performCombine(identifier_type, words)

def performSplit(word):
    result = ""
    if word[-2:] == "()":
        word = word[:-2]
    if word[0].isupper():
        word = word[0].lower() + word[1:]
    for letter in word:
        if letter.isupper():
            result += " "
        result += letter.lower()
    return result

def performCombine(identifier_type, words):
    result = ""
    words = words.split(" ")
    
    if identifier_type == 'M':
        result += words[0]
        for word in words[1:]:
            result += word.capitalize()
        result += "()"
        
    if identifier_type == 'C':
        for word in words:
            result += word.capitalize()
        
    if identifier_type == 'V':
        result += words[0]
        for word in words[1:]:
            result += word.capitalize()
        
    return result

if __name__ == '__main__':
    arr = []
    while True:
        try:
            line = input().rstrip()
        except:
            break
        result = generateResult(line)
        print(result)
