"""
file: data_generator.py
description: Generate data (uniform and normal distribution) 
to test using different sort algorithms.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""

import numpy as np

number_of_tests = 100
mu, sigma = 0.5, 0.0001


def generate_tests_data(arr_size, number_of_tests):
    uniform_str = ""
    normal_str = ""

    for i in range(number_of_tests):

        s_normal = np.random.normal(mu, sigma, arr_size)
        s_uniform = np.random.uniform(0, 1, arr_size)

        uniform_str_temp = ""
        normal_str_temp = ""

        for i in range(arr_size):
            uniform_str_temp += str(s_uniform[i]) + " "
            normal_str_temp += str(s_normal[i]) + " "

        uniform_str += uniform_str_temp + "\n"
        normal_str += normal_str_temp + "\n"

    f_uni = open("uniform_input_"+str(arr_size), "w")
    f_nor = open("normal_input_"+str(arr_size), "w")
    f_uni.write(uniform_str)
    f_nor.write(normal_str)
    f_uni.close()
    f_nor.close()


generate_tests_data(100, 100)
generate_tests_data(1000, 100)
generate_tests_data(10000, 100)
generate_tests_data(100000, 100)
