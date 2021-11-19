"""
file: backsplash.py
description: Determine how many overall patterns there
are with which you can tile your backsplash using the pieces
provided.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""

"""
The function process input provided and returns n, 
the width of the backsplash. 

:param: None
:return: width of the backsplash
"""

def process_input():
    num_columns = int(input())
    return num_columns

"""
The main function process input provided and 
returns number of possible tilings for the given backsplash. 

:param: None
:return: total combinations of tilings for the given input
"""
def main():
    num_columns = process_input()

    total_combinations = [1, 1, 5, 11]

    for column in range(4, num_columns + 1):
        total_combinations.append(
            total_combinations[column - 1] + 4 * total_combinations[column - 2] + 2 * total_combinations[column - 3])

    print(total_combinations[num_columns])


if __name__ == '__main__':
    main()
