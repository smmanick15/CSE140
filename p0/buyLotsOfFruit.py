#!/usr/bin/env python3

"""
Based off of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

To run this script, type:

  python3 buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""
   
FRUIT_PRICES = {
    'apples': 2.00,
    'oranges': 1.50,
    'pears': 1.75,
    'limes': 0.75,
    'strawberries': 1.00
}

def buyLotsOfFruit(orderList):
    """
    orderList: List of (fruit, weight) tuples

    Returns cost of order
    """

    i = 0                   # to track iterations in fruit list
    order_cost = 0.0        # to track cost of fruit

    while i < len(orderList):
        if orderList[i][0] in FRUIT_PRICES:
            order_cost = order_cost + (orderList[i][1] * (FRUIT_PRICES[orderList[i][0]]))
        else:
            print("You are trying to buy fruit that this store doesn't sell... Please try your local Farmers Market!")
            return None
        i = i+1

    return order_cost

def main():
    orderList = [
        ('apples', 2.0),
        ('pears', 3.0),
        ('limes', 4.0)
    ]

    print("Cost of %s is %s." % (orderList, buyLotsOfFruit(orderList)))

if __name__ == '__main__':
    main()
