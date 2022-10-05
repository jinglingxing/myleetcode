#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:17:47 2020

@author: jinlingxing
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #dictionary
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        #enumerate all the chars in words
        for c in word:
            if c not in p:
                #create new dictionary 
                p[c] = {}
                #move to p[c]
            p = p[c]
        # it's the end of this word 
        p['#'] = True
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        #check if the node is not empty and if it's the end of word
        return node is not None and '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        #self.find(prefix) is none which means it's not a prefix
        return self.find(prefix) is not None
    def find(self, prefix:str) -> set:
        """
        Returns the trie node start of prefix, if there is no word in the trie that starts with the given prefix returns none
        """
        p = self.root
        for c in prefix:
            if c not in p:
                return None
            p = p[c]
        return p
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)