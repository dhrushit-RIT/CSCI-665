"""
    file: largestSum.py
    description: Determine minimum cost to seat all the people from line both line on the ride.
    language: python3
    author: Dhrushit Raval - dr9703@g.rit.edu
    author: Julia Sanguinetti - js8848@rit.edu
"""


def process_input():
    """
    input content:
        length of the array
        array
    :return: array
    """
    num_input = int(input())
    a = []
    arr = [int(x) for x in input().strip().split()]
    arr.insert(0, None)
    return arr


def process_dummy_input():
    """
    for testing purposes only
    directly return the list of numbers
    :return:
    """
    input_array = [None, 3, -7, -4, 1, 5, 2, 6, 1]
    # input_array = [None, 1, 6, 3, 4, 8, 7, 2]
    # input_array = [None, 10, 8, 1, 2, 4, 9, 7]
    return input_array


def find_largest_sum_for_increasing_subsequence(input_array):
    """
    finds increasing subsequence with the largest sum
    :param input_array: array to check on
    :return: largest sum
    """
    max_sum = [0]

    if input_array[0] is not None:
        input_array.insert(0, None)
    # [None, 2, 4, 7, 1, 5]

    for i in range(1, len(input_array)):
        max_sum_val = 0
        max_sum_index = 0
        for j in range(i):
            if input_array[j] is not None:
                if input_array[i] > input_array[j]:
                    if max_sum_val < max_sum[j]:
                        max_sum_val = max_sum[j]
                        max_sum_index = j
            else:
                max_sum_val = 0
                max_sum_index = 0
        max_sum.append(max_sum[max_sum_index] + input_array[i])

    return max(max_sum), max_sum


def trace_max_sum(input_arr, max_sum_arr, max_sum):
    """
    traces how you get max sum of the increasing subsequence
    :param input_arr: source array
    :param max_sum_arr: array of elements in max sum
    :param max_sum: value of max sum
    :return:
    """
    curr_max = max_sum
    trace = []
    for i in range(len(max_sum_arr) - 1, 0, -1):
        if curr_max == 0:
            break
        if max_sum_arr[i] != curr_max:
            continue
        else:
            trace.append(i)
            curr_max -= input_arr[i]

    return trace


def main():
    # input_array = process_dummy_input()
    input_array = process_input()
    max_sum, max_sum_arr = find_largest_sum_for_increasing_subsequence(input_array)
    max_sum_trace = trace_max_sum(input_array, max_sum_arr, max_sum)
    print(max_sum)
    # print("input =", input_array)
    # print("max_sum =", max_sum)
    # print("max_sum_arr =", max_sum_arr)
    # print("trace max sum =", max_sum_trace)
    # print("trace max sum =", [input_array[x] for x in max_sum_trace])


if __name__ == '__main__':
    main()
