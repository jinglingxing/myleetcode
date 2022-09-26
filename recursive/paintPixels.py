#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:44:49 2020

@author: jinlingxing
"""
'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
   Hide Hint #1  
Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.

'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.paintPixels(image,sr,sc,newColor)
        return image
    
    def paintPixels(self, image, sr, sc, newColor):
        preColor = image[sr][sc]
        if preColor == newColor :
            return
        image[sr][sc] = newColor
        if 0<=sr-1 and image[sr-1][sc] == preColor:
            self.paintPixels(image, sr-1, sc, newColor)
        if sr+1<len(image) and image[sr+1][sc] == preColor: 
            self.paintPixels(image, sr+1, sc, newColor)
        if 0<=sc-1 and image[sr][sc-1] == preColor:
            self.paintPixels(image, sr, sc-1, newColor)
        if sc+1<len(image[0]) and image[sr][sc+1] == preColor:
            self.paintPixels(image, sr, sc+1, newColor)
        return
        