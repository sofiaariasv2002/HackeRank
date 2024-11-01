##################################################################################################################
# Sofia Arias villa
# HackeRank - interview preparation kit (sorting)
# 31 oct 2024
##################################################################################################################

##################################################################################################################
# Mark and Jane are very happy after having their first child. 
# Their son loves toys, so Mark wants to buy some. 
# There are a number of different toys lying in front of him, tagged with their prices. 
# Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. 
# Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

#Note Each toy can be purchased only once.
##################################################################################################################

def maximumToys(prices, k):
    prices.sort()
    sum=0
    cant=0
    for price in range(len(prices)):
        sum+=prices[price]
        if sum < k:
            cant+=1
        else:
            return (cant)


if __name__ == '__main__':
    k=7
    prices=[1, 2, 3, 4]
    #prices=[1, 12, 5, 111, 200, 1000, 10]
    print(maximumToys(prices, k))