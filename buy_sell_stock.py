def maxProfit(prices):
    maximum = 0
    minimum = prices[0]

    for i in range(len(prices)):
        minimum = min(minimum, prices[i])
        maximum = max(maximum, prices[i] - minimum)
    return maximum


print(maxProfit([7,1,5,3,6,4]))