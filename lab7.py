from time import time


def DACcoins(coins, amount):
    if amount == 0: #base case
        return 0
    else:
        minCoins = float('inf')
        for currentCoin in coins: #check all coins
            #If we can give change
            if (amount - currentCoin) >= 0:
                #calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) +1
                #keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins


def DPcoins(coins, amount):
    #create initial tables
    minCoins = [float('inf') for i in range(0, amount+1)]
    traceback = [[] for i in range(0, amount+1)]
    minCoins[0] = 0
    traceback[0] = 0
    #base case
    if amount <= 0:
        print("Select a valid amount")

    #Min required
    # 1 2 3 4 5 6 ..
    # 1 2 3 4 1 2
    #Which coins
    # 1  2  3  4  5  6      7 ...
    # 1p 2p 3p 4p 1n 1n1p   1n2p

    #traceback is winner table, append the best option
    #minCoins is how many coins per amount, traceback is what the min # of coins actually are
    for value in range(0, amount + 1):
        for mycoin in coins:
            if value - mycoin >= 0:
                minCoins[value] = min(minCoins[value], minCoins[value-mycoin]+1)
    return minCoins[amount]
#figure out each variety for coins you can use, select the one with the shortest length?

print(DPcoins([1,5,10,12,25], 29))