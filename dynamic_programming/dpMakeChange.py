# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 13:14:39 2017

@author: Jinling
"""
#coinCount 是与列表中的位置相对应进行找零的最小硬币数。
#coinsUsed 是用于找零的硬币的列表
#printCoins 通过表打印出使用的每个硬币的值
def dpMakeChange(coinValueList,change,minCoins,coinUsed):
    for cents in range(change+1):
        coinCount= cents
        newCoin=1
        for j in [c for c in coinValueList if c<= cents]:
            if minCoins[cents - j] +1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin=j
        minCoins[cents] = coinCount
        coinUsed [cents] = newCoin
        
    return minCoins[change]

def printCoins(coinUsed, change):
    coin = change
    while coin>0:
        thiscoin = coinUsed[coin]
        print(thiscoin)
        coin = coin - thiscoin
                
def main():
    amnt= 63
    clist= [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)
    
    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)
    
main()