"""
file: snowfall.py
description: Determine if there exists a three-day interval
that produced more than half of the total snowfall across the n days.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""

"""
This function returns an array containing each of the 
cumulative sums of snowfall contained in the input provided.
:param: None.
:return: array containing all cumulative sums of snowfall 
based on input provided
"""
def process_input():
    number_of_days = int(input())

    cumulative_sum = input().strip().split()
    cumulative_sum = [int(x) for x in cumulative_sum]

    return cumulative_sum

"""
The function calculates the total sum of snowfall present in
the array, divides it by half and stores it in variable
required_sum. By running binary search, it searches the array
cumulative_sum to determine whether it contains any 3 
consecutive values that display a value that is greater than
the required_sum. 

:param: cumulative_sum 
:return: None
"""
def find_interval(cumulative_sum):
    arr_size = len(cumulative_sum)
    required_sum = cumulative_sum[arr_size-1]/2
    left = 0
    right = arr_size-1

    while True:
        if left == right:
            return True

        mid = (right + left) // 2

        if cumulative_sum[mid] - cumulative_sum[left] <= required_sum and cumulative_sum[right] - cumulative_sum[mid] <= required_sum and cumulative_sum[right] - cumulative_sum[left] <= required_sum:
            return False
        else:
            # handling mid ranges
            for i in range(4):
                if mid - i >= 0 and (mid + 3 - i) < arr_size:
                    if cumulative_sum[mid - i + 3] - cumulative_sum[mid - i] > required_sum:
                        return True
            
            if right - left <= 3:
                return True
            if cumulative_sum[mid] - cumulative_sum[left] > required_sum:
                right = mid
            else:# cumulative_sum[right] - cumulative_sum[mid] > required_sum:
                left = mid

"""
The main function calls process_input to get the array 
containing the cumulative values of snowfall. It then 
creates a boolean variable has_interval that represents 
the output of the function find_interval after the binary 
search was done on cumulative_sum. The main function returns 
"YES" if there exists a three-day interval that produced 
more than half of the total snowfall across the n days 
based on binary search from find_interval. It returns "NO"
otherwise.

:param: None
:return: "YES" if has_interval is True, "NO" otherwise.
"""
if __name__ == "__main__":
    cumulative_sum = process_input()
    has_interval = find_interval(cumulative_sum)
    if has_interval:
        print("YES")
    else:
        print("NO")
    pass
