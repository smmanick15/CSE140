#!/usr/bin/env python3

"""
Based of of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders: [('apples', 1.0), ('oranges', 3.0)] best shop is shop1.
For orders: [('apples', 3.0)] best shop is shop2.
"""

import shop

def shopSmart(orderList, fruitShops):
    """
    orderList: List of (fruit, numPound) tuples
    fruitShops: List of FruitShops
    """

    # *** Your Code Here ***

    print(type(fruitShops[0]))
    best_shop = fruitShops[0]
    print("here we are testing the variable::: ------->", best_shop.name)

    i = 0
    lowest_cost = 0
    best_shop = fruitShops[0]

    current_cost = 0
    current_shop = fruitShops[0]

    while i < len(fruitShops):
        j = 0
        while j < len(orderList):
            print("printing inside loop")
            print(orderList[j])
            j = j+1
        #for fruit in orderList:
            #print(orderList([fruit]))
            #current_cost = current_cost + ((fruitShops[i].fruitPrices(orderList[fruit][1]))* (orderList[fruit][1]))
        #print("the current cost for: ", fruitShops[i].name, "is: $", current_cost)

        i=i+1

    #print(orderList)
    #print(type(fruitShops[0].fruitPrices))
    #print(orderList[0][0])
    #if orderList[0][0] in fruitShops[0].fruitPrices:
    #    print("fruit price found: $", fruitShops[0].fruitPrices[orderList[0][0]])
    #else:
    #    print("fruit price not found")


    '''i = 0
    order_cost = 0.0

    while i < len(orderList):
        if orderList[i][0] in FRUIT_PRICES:
            order_cost = order_cost + (orderList[i][1] * (FRUIT_PRICES[orderList[i][0]]))
        else:
            print("You are trying to buy fruit that this store doesn't sell... Please try your local Farmers Market!")
            return None
        i = i+1

    return order_cost'''   
    
    return fruitShops[0]

def main():
    dir1 = {
        'apples': 2.0,
        'oranges': 1.0
    }

    dir2 = {
        'apples': 1.0,
        'oranges': 5.0
    }

    shop1 =  shop.FruitShop('shop1', dir1)
    shop2 = shop.FruitShop('shop2', dir2)

    shops = [shop1, shop2]

    orders = [('apples', 1.0), ('oranges', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

    orders = [('apples', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

if __name__ == '__main__':
    main()
