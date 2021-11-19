"""
file: time_analysis.py
description: Analyse the running time for three sorting
algorithms.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""


from validator import validate_sequence
from numpy import average
from sortingTest import bucket_sort, insertion_sort, merge_sort
import matplotlib.pyplot as plt
import time

UNIFORM_DATA = "uniform"
NORMAL_DATA = "normal"

arr_size = 100000

"""
The function takes an input array and sorts is using
merge sort. It then calculates the running time and
returns it.

:param: array (input data) to analyse 
:return: running time of mergesort algorithm
"""
def test_merge_sort(input_arr):
    mergesort_time = time.time()
    sorted_sequence = merge_sort(input_arr)
    mergesort_time = time.time() - mergesort_time
    return mergesort_time

"""
The function takes an input array and sorts is using
bucket sort. It then calculates the running time and
returns it.  

:param: array (input data) to analyse 
:return: running time of bucket sort algorithm
"""
def test_bucket_sort(input_arr):
    bucketsort_time = time.time()
    bucket_sort(input_arr)
    bucketsort_time = time.time() - bucketsort_time
    return bucketsort_time
"""
The function takes an input array and sorts is using
insertion sort. It then calculates the running time and
returns it.  

:param: array (input data) to analyse 
:return: running time of insertion sort algorithm
"""

def test_insertion_sort(input_arr):
    insertionsort_time = time.time()
    insertion_sort(input_arr)
    insertionsort_time = time.time() - insertionsort_time
    return insertionsort_time
"""
The function takes an input array and apply
 all sorting algorithms, calculating their running
 time
:param: array (input data) to analyse 
:return: all running times for all sorting algorithm
"""

def test_input(input_arr):
    msort_time = 0
    bsort_time = 0
    isort_time = 0
    msort_time = test_merge_sort(input_arr)
    bsort_time = test_bucket_sort(input_arr)
    if len(input_arr) <= 1000:
        isort_time = test_insertion_sort(input_arr)

    return (msort_time, bsort_time, isort_time)


"""
The main function calls reads the file (input) line by line
and apply all sorting algorithms while calculating and printing 
out their running times.

:param: None
:return: None
"""
if __name__ == "__main__":


    for data_type in ["uniform", "normal"]:
        merge_sort_time = []
        bucket_sort_time = []
        insertion_sort_time = []
        file_name = data_type + "_input_" + str(arr_size)

        with open(file_name) as f:
            for line in f:
                input_arr = line.strip().split()
                input_arr = [float(x) for x in input_arr]
                m, b, i = test_input(input_arr)
                # merge_sort_time.append(m)
                bucket_sort_time.append(b)
                # insertion_sort_time.append(i)

        print(data_type.upper(),"    n=",arr_size, "    average over 100 tests" )
        print("--------------------------------------------------------------------------")
        print("Merge sort : ", average(merge_sort_time))
        print("Bucket sort : ", average(bucket_sort_time))
        print("Insertion sort : ", average(insertion_sort_time))
        print()

