import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_percent=meal_cost*tip_percent/100
    tax_percent=meal_cost*tax_percent/100
    totalmealcost=meal_cost+tip_percent+tax_percent
    totalmealcost=int(round(totalmealcost))
    return totalmealcost


if __name__ == '__main__':
    meal_cost = float(input("Enter Meal_Cost: " ))

    tip_percent = int(input("Enter Tip_percentage in Integer: "))

    tax_percent = int(input("Enter Tax_percentage in Integer: "))

    print(solve(meal_cost, tip_percent, tax_percent))
