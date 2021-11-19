"""
file: candy.py
description: Determine the maximum number of different types
of candy that can be bought with one's allowance.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""

import random

"""
The function process input provided and returns allowance 
together with an array containing the cost for each candy. 

:param: None
:return: allowance from given input and array containing the cost for each candy
"""
def process_input():
    allowance = int(input())
    total_candies = int(input())
    candy_costs = [int(cost) for cost in input().strip().split()]
    return allowance, candy_costs

"""
The function uses k select algorithm to choose a value from the array 
as pivot and divide the data in half as less than or greater than the pivot 
recursively. 

:param: allowance, array containing candy costs
:return: total from adding the values that are less, equal and something from the greater array
"""
def max_candies_recursive(allowance, arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        if arr[0] > allowance:
            return 0
        else:
            return 1
    random_pivot = random.randrange(len(arr))

    lesser = [element for element in arr if element < arr[random_pivot]]
    equal = [element for element in arr if element == arr[random_pivot]]
    greater = [element for element in arr if element > arr[random_pivot]]

    lesser_sum = sum(lesser)
    equal_sum = sum(equal)
    greater_sum = sum(greater)

    if lesser_sum > allowance:
        return max_candies_recursive(allowance, lesser)
    elif lesser_sum == allowance:
        return len(lesser)
    else:
        remaining_allowance = allowance - lesser_sum
        if equal_sum > remaining_allowance:
            return len(lesser) + int(remaining_allowance / equal_sum * len(equal))
        elif equal_sum == remaining_allowance:
            return len(lesser) + len(equal)
        else:
            remaining_allowance = allowance - lesser_sum - equal_sum
            return len(lesser) + len(equal) + max_candies_recursive(remaining_allowance, greater)

"""
The function calculates max number of types 
that can be purchased with allowance

:param: allowance, array containing candy costs
:return: None
"""
def max_candies(allowance, candy_costs):
    filtered_array = [candy_cost for candy_cost in candy_costs if candy_cost <= allowance]

    print(max_candies_recursive(allowance, filtered_array))


def main():
    allowance, candy_costs = process_input()
    max_candies(allowance, candy_costs)


if __name__ == '__main__':
    main()
