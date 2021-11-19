"""
file: sorting.py
description: implementation of sorting algorithms.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""

from validator import validate_sequence
import time
import math

"""
This function sorts the data by using merge sort algorithm. 
:param: data to be sorted 
:return: sorted data array
"""
def merge_sort(data):

    if len(data) == 1:
        return data

    mid_index = len(data)//2

    left_array = merge_sort(data[:mid_index])
    right_array = merge_sort(data[mid_index:])

    return_data = []
    left_array_index = 0
    right_array_index = 0

    while left_array_index < len(left_array) and right_array_index < len(right_array):
        if left_array[left_array_index] < right_array[right_array_index]:
            return_data.append(left_array[left_array_index])
            left_array_index += 1
        else:
            return_data.append(right_array[right_array_index])
            right_array_index += 1

    if left_array_index < len(left_array):
        return_data.extend(left_array[left_array_index:])

    if right_array_index < len(right_array):
        return_data.extend(right_array[right_array_index:])

    return return_data

"""
This function sorts the data by using using insertion sort. 

:param: data to be sorted 
:return: sorted data array
"""

def insertion_sort_2(data):
    for i in range(1, len(data), 1):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                (data[j-1], data[j]) = (data[j], data[j-1])
            else:
                continue

def insertion_sort(data):
    """
    classic insertion sort. reference taken from Geeks For Geeks
    """
    for i in range(1, len(data)):
        # print("-----xxxxx-----xxxxx-----xxxxx-----xxxxx-----xxxxx-----")
        item_to_move_to_sorted_array = data[i]

        j = i - 1
        while j >= 0 and item_to_move_to_sorted_array < data[j] :
                data[j + 1] = data[j]
                j -= 1
        data[j + 1] = item_to_move_to_sorted_array
    return data

"""
This function sorts the data by using using bucket sort. 

:param: data to be sorted 
:return: sorted data array
"""

def bucket_sort(data):
    num_buckets = len(data)

    t1 = time.time()

    buckets = [[] for _ in range(num_buckets)]
    t2 = time.time()
    for item in data:
        bucket_index = int(item*num_buckets)
        buckets[bucket_index].append(item)

    for bucket in buckets:
        bucket = insertion_sort(bucket)

    sorted_data = []
    for bucket in buckets:
        sorted_data += bucket

    return sorted_data

"""
The main function calls all sorting algorithms (bucket sort, 
merger sort and insertion sort) in a data distribution
while calculating the running time for each of them.

:param: None
:return: None
"""
if __name__ == "__main__":

    bucket_sort_time = time.time()
    sorted = bucket_sort([0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0])
    validate_sequence(sorted)
    bucket_sort_time = time.time() - bucket_sort_time
    print("bucket sort time:", bucket_sort_time)

    merge_sort_time = time.time()
    sorted = merge_sort([0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0])
    validate_sequence(sorted)
    merge_sort_time = time.time() - merge_sort_time
    print("merge sort time:", merge_sort_time)

    insertion_sort_time = time.time()
    sorted = insertion_sort([0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0])
    validate_sequence(sorted)
    insertion_sort_time = time.time() - insertion_sort_time
    print("insertion sort:", insertion_sort_time)
