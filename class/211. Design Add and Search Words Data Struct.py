#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:21:47 2020

@author: jinlingxing
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #set a dictionary as data structure
        self.root = {}
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['#'] = True
                             

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        root = self.root
        return self.find(root, word)
    
    def find(self, root, word:str) -> bool:
        if not word:
            if '#' in root:
                return True
            else:
                return False
        if word[0] == '.':
            for w in root:
                if w!='#' and self.find(root[w], word[1:]) :
                    return True
        else:
            #if word or subword is not starting with a dot
            if word[0] in root:
                return self.find(root[word[0]] ,word[1:])            
        return False
                           
#["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
#[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]              

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
w1 = "at"
w2 = "and"
w3 = "an"
w4 = "add"
w5 = "bat"
obj.addWord(w1)
obj.addWord(w2)
obj.addWord(w3)
obj.addWord(w4)
obj.addWord(w5)

word1 = "a"
word2 = ".at"
word3 = ".at"
word4 = "ad."
word5 = "a.d."
word6 = "b."
word7 = "a.d"
word8 = "."
#search1 = obj.search(word1)
search2 = obj.search(word2)
#search3 = obj.search(word3)
#search4 = obj.search(word4)
#search5 = obj.search(word5)
#search6 = obj.search(word6)
#search7 = obj.search(word7)
#search8 = obj.search(word8)