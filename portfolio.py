from pandas import *

def printMatrix(m):
    for row in m:
        print(row)

def loadData(filename):
    """
    Loads in data as dictionary, returns region, cost, gain
    """
    metro = read_csv(filename)
    regionDict = {}
    for region, cost, gain in zip(list(metro['RegionName']), list(metro['2020-01']),
                                 list(metro['2020-01'] - metro['2019-01'])):
        regionDict[region] = cost, gain
    return regionDict

def optimizeInvestments(regionDict, totMoney):
    n = len(regionDict)
    # list of gains from the dictionary
    gains = []
    for value in regionDict.values():
        gains.append(value[1])

    # list of cost from the dictionary
    cost = []
    for value in regionDict.values():
        cost.append(value[0])

    regionList = []
    for value in regionDict.keys():
        regionList.append(value)

    # m is matrix of investments x money to store max gain
    # traceback is matrix of investments x money to store winning region

    m = [[None for i in range(totMoney + 1)] for j in range(n + 1)]
    traceback = [[None for i in range(totMoney + 1)] for j in range(n + 1)]

    # Fill in the rest of the table diagonal by diagonal
    for region in range(n + 1):
        for value in range(totMoney + 1):
            #base case; if we select 0 investments or have no money
            if region == 0 or value == 0:
                m[region][value] = 0
                traceback[region][value] = 0
            elif cost[region-1] <= value:
                m[region][value] = max(gains[region-1] + m[region-1][value-cost[region-1]], m[region-1][value])
                traceback[region][value] = regionList[region-1]
                #print(regionList[region-1])
            else:
                m[region][value] = m[region-1][value]
                #print(regionList[region-1])
                traceback[region][value] = regionList[region-1]

    currentRegion = m[n][totMoney]
    for i in range(0, currentRegion):
        print(f'{traceback[n][totMoney]}')
        currentRegion =


stuff = loadData("minimetro.csv")
print(optimizeInvestments(stuff, 1000000))