#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:34:45 2020

@author: jinlingxing
"""
'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
'''

class Solution(object):
    def invalidTransactions(self, transactions):
        if not transactions:
            return []
        
#        memo = collections.defaultdict(list)    #create a dictionary to keep track of previous transaction 
        memo = {}
        invalid_tran = set()                    #to store invalid transaction / I use set to avoid duplication
        for i,transaction  in enumerate (transactions):
            
            name, time, amount, city = (int(i) if i.isnumeric() else i for i in transaction.split(','))
            
            if amount > 1000:                   #if the amount is greater than 1000 add it to the invalid_tran
                invalid_tran.add(transaction)               
                 
            if name in memo:                    # if there is any other previous transaction done by similar person , check it from the memo
                for tran in memo[name]:         # bring all previous transaction done by similar person (iterate over the memo)
                    _, prev_time, _, prev_city =(int(i) if i.isnumeric() else i for i in  tran.split(','))
                    if abs(time-prev_time) <= 60 and prev_city != city:  #check if the absolute time difference is less than 60 and the city is the same
                        invalid_tran.add(tran) 
                        invalid_tran.add(transaction)                    
            if name not in memo:
                memo[name] = []
            memo[name].append(transaction)  # add the transaction to the dictionary (memo) - always keep track of previous transaction 
        return invalid_tran
        



        
sol = Solution()
transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
sol.invalidTransactions(transactions)