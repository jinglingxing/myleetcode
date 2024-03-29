#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:04:37 2020

@author: jinlingxing
"""
'''
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:

Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]

Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1

 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
   Hide Hint #1  
Use doubly Linked All kind of LIST with hashmap of pointers to linked All kind of LIST nodes. add unique number to the linked All kind of LIST. When add is called check if the added number is unique then it have to be added to the linked All kind of LIST and if it is repeated remove it from the linked All kind of LIST if exists. When showFirstUnique is called retrieve the head of the linked All kind of LIST.
   Hide Hint #2  
Use queue and check that first element of the queue is always unique.
   Hide Hint #3  
Use set or heap to make running time of each function O(logn).

'''

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.dictN = {} #key is number; value is frequency
        for i in nums: #put all nums in q and dict
            self.add(i)

    def showFirstUnique(self) -> int:
        #check if the first value is unique       
        while len(self.q)>=1 and self.dictN[self.q[0]]>1:
            self.q.pop(0) #delete the not unique values
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]
    def add(self, value: int) -> None:
        if value in self.dictN:
            self.dictN[value] += 1 #if the value(number) exists, frequency +=1
        else:
            self.dictN[value] = 1 
            self.q.append(value) #add the number in the queue
            
