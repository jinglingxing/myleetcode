#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:19:37 2020

@author: jinlingxing
"""

class StockSpanner:
    def __init__(self):
        self.l = []

    def next(self, price: int) -> int:
        count = 1
        while self.l and self.l[-1][0]<=price:
            pre_price, pre_count = self.l.pop()
            count += pre_count
        self.l.append((price,count))
        
        return self.l[-1][1]

    


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
sol = StockSpanner()
sol.next(3)
sol.next(5)
sol.next(8)
sol.next(8)
