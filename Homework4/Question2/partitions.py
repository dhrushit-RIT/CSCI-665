"""
    file: partitions.py
    description: Finds the number of even and odd partitions possible from a list of numbers
    language: python3
    author: Dhrushit Raval - dr9703@g.rit.edu
    author: Julia Sanguinetti - js8848@rit.edu
"""


def process_dummy_input():
    """
        for testing purposes only
        directly return the line configurations in the form of tuple of two strings
        :return:
    """
    # return [4, 8, 6, 2, 0, 8, 6] # 4.1 64,0
    # return [3, 6, 4, 8, 2, 6, 8] # 4.2 0,1
    # return [3, 6, 4, 8, 2, 6, 8, 5] # 4.3 1,7
    # return [77, 12, 24, 2, 78, 16, 11, 79, 47, 39, 64, 18, 18, 37, 94, 71, 73, 99, 78, 3, 48, 22, 67, 70, 71 ] # 4.4 256,10173
    # return [4, 1, 2, 6, 4, 3, 2, 6, 1, 6, 7, 7, 8, 5, 7, 4, 3, 6, 5, 6, 4, 3, 6, 4, 3, 6, 5, 1, 4, 3, 6, 7, 6, 0, 0, 5,
    #         2, 1, 6, 1]  # 4.5 65536, 5894011
    # return [1, 2, 2,2,1, 1]


def process_input():
    """
    processes input to feed to algorithm
    :return: array of int numbers
    """
    arr_size = int(input())
    num_array = [int(x) for x in input().strip().split()]
    return num_array


def find_even_partitions(arr):
    """
    finds the number of even partitions possible in the list of numbers
    :param arr: input array
    :return: num even partitions possible
    """
    """
        even-partitions
        1: 1
        2: 3
        3: 4
        4: 8
        5: 16 ...
        """

    cnt_even = 0
    cnt_odd = 0
    for i in arr:
        if i & 1:
            cnt_odd += 1
        else:
            cnt_even += 1

    num_even = 0
    num_odd = 0
    for num in arr:
        if num & 1:
            if num_odd == 1:
                num_even += 1
                num_odd = 0
            else:
                num_odd = 1
        else:
            if num_odd == 0:
                num_even += 1

    even_partitions = [1, 3, 4]
    for i in range(2, num_even):
        even_partitions.append(2 * even_partitions[-1])

    if num_odd & 1:
        return 0
    else:
        return even_partitions[num_even - 1]


def find_odd_partitions(arr):
    """
    finds the number of odd partitions possible in the list of numbers
    :param arr: input array
    :return: num odd partitions possible
    """
    odd_partitions_array = [0]
    last_odd_index = -1
    value = 1
    for i in range(len(arr)):
        if arr[i] & 1:
            odd_partitions_array.append(value)
            value = odd_partitions_array[-1] + odd_partitions_array[-2]
            last_odd_index = i
        else:
            value += odd_partitions_array[-1]
            odd_partitions_array.append(odd_partitions_array[-1])

    return odd_partitions_array[-1]


def find_partitions(arr):
    """
    finds odd and even partitions possible in the list
    :param arr: input array to find partitions for
    :return: tuple of (even_partitions_count, odd_partitions_count)
    """
    num_even_partitions = find_even_partitions(arr)
    """
    odd-partitions
    """
    num_odd_partitions = find_odd_partitions(arr)

    return num_even_partitions, num_odd_partitions


def main():
    """
    main driver function
    """
    arr = process_input()
    # arr = [1,1,1,1,1,1]
    # arr = process_dummy_input()
    num_even_partitions, num_odd_partitions = find_partitions(arr)
    print(num_even_partitions)
    print(num_odd_partitions)


if __name__ == '__main__':
    main()
