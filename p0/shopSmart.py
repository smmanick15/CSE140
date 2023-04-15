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

    
    i = 0
    lowest_cost = 0             # tracks value of lowest cost total
    best_shop = fruitShops[0]   # contains fruit shop with lowest cost

    while i < len(fruitShops):
        j = 0
        current_cost = 0
        current_shop = fruitShops[i]
        #print("currently we are calculating the total cost at: ", fruitShops[i].name, "for the list: ", orderList)
        
        #this while loop calculates the total cost of the fruit in the list at the current shop
        while j < len(orderList):
            #print("calculating the cost of the first fruit in the list:")
            fruit_cost = orderList[j][1] * fruitShops[i].fruitPrices[orderList[j][0]]
            #print("the cost for this iteration of fruit is: $", fruit_cost)
            current_cost = current_cost + (orderList[j][1] * fruitShops[i].fruitPrices[orderList[j][0]])
            #print("current total cost: $", current_cost)
            j = j+1

        #the following logic sequence compares the current cost to the lowest cost shop
        if (current_cost < lowest_cost):
            lowest_cost = current_cost
            best_shop = current_shop
        
        if (lowest_cost == 0):      #if this is the first shop iteration in the loop
            lowest_cost = current_cost
            best_shop = current_shop
        
        
        i=i+1
   
    
    return best_shop

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
