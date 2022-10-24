for value in range(0, amount + 1):
    for mycoin in coins:
        if value - mycoin >= 0:
            currentMin = minCoins[value - mycoin] + 1
            if currentMin < minCoins[value]:
                minCoins[i] = currentMin
                traceback[i] = currentCoin

                for value in range(0, amount + 1):
                    for mycoin in coins:
                        if value - mycoin >= 0:
                            minCoins[value] = min(minCoins[value],
                                                  minCoins[value - mycoin] + 1)
                return minCoins[amount]