"""
    file: headache.py
    description: Determine minimum cost to seat all the people from line both line on the ride.
    language: python3
    author: Dhrushit Raval - dr9703@g.rit.edu
    author: Julia Sanguinetti - js8848@rit.edu
"""


def process_input():
    """
    processes the input and feeds it to the program
    line 1 : the number of people in line one
    line 2 : the number of people in line two
    line 3 : people in line one
    line 4 : people in line two
    :return: tuple of strings representing line one and line two people
    """
    m = int(input())
    n = int(input())

    string1 = input().strip()
    string2 = input().strip()

    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    return string1, string2


def process_dummy_input():
    """
    for testing purposes only
    directly return the line configurations in the form of tuple of two strings
    :return:
    """
    # # 4.0 - 4
    # string1 = "E E N"
    # string2 = "N N V E"

    # 4.1 - 3
    string2 = "V V N E"
    string1 = "N E V"

    # # 4.2 - 5
    # string1 = "E N E"
    # string2 = "N N"

    # # 4.3 - 4
    # string1 = "E N"
    # string2 = "E N E"

    # # 4.4 - 7 wrong if 4.2 correct
    # string1 = "N V V E E E N N E E E N V"
    # string2 = "E V N V N E V N E E N"

    # # 4.5 - 27 wrong if 4.2 correct
    # string1 = "N N N V V V E E E E V V V N N N N N N N E E E E E N N N N N N N V V V V V N N N"
    # string2 = "V N E V N E V N E V N E V N E V N E V N E V N E V N E V N E V N E V N"

    # return "NEE", "EVNN" # 4
    # return "ENVV", "VEN" # 3
    # return "N V V E E E N N E E E N V"[::-1].replace(" ", ""), "E V N V N E V N E E N"[::-1].replace(" ", "") # 7

    #
    # do not change anything below this line for this function
    #
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    return string1, string2


def pairing_cost(rider1=None, rider2=None):
    """
    calculates the cost of pairing two people for the ride
    rider types : E N V
    :param rider1: type of first rider
    :param rider2: type of second rider
    :return: cost of pairing rider 1 and rider 2 on the ride
    """
    if rider1 is None and rider2 is not None or rider2 is None and rider1 is not None:
        return 4

    if rider1 == 'E' and rider2 == 'N' or rider1 == 'N' and rider2 == 'E':
        return 5

    return 0


def print_arr(s, l1, l2):
    """
    for testing purposes only
    prints the dynamic programming array representing the costs
    :param s: the array that stores the cost
    :param l1: length of the line 1
    :param l2: length of line 2
    :return: None
    """
    for i in range(l1 - 1, -1, -1):
        for j in range(l2):
            print(s[i][j], end=" ")
        print()
    print()


def find_min_headache(string1, string2, penalty_en, gap_penalty, gap_2_penalty):
    """
    finds the minimum total headache so that everyone from both the lines can sit on the ride
    :param string1: line 1 configuration
    :param string2: line 2 configuration
    :param penalty_en: cost of pairing E type and N type
    :param gap_penalty: cost of sending a person solo on the ride if there are more people in either lines
    :param gap_2_penalty: cost of sending a pair from one of the lines if there are some people in the other line
    :return: minimum cost so that everyone is able to sit on the ride
    """
    t_string1 = " " + string1[:]
    t_string2 = " " + string2[:]

    s = [[0] * (len(string2) + 1) for _ in range((len(string1) + 1))]

    for i in range(1, len(t_string1)):
        solo = 0 if i <= 1 else (gap_penalty + s[i - 1][0])
        pair = solo if i <= 1 else (pairing_cost(t_string1[i], t_string1[i - 1]) + s[i - 2][0])

        s[i][0] = min(solo, pair)

    for i in range(1, len(t_string2)):
        solo = 0 if i <= 1 else (gap_penalty + s[0][i - 1])
        pair = solo if i <= 1 else (pairing_cost(t_string2[i], t_string2[i - 1]) + s[0][i - 2])

        s[0][i] = min(solo, pair)

    for i in range(1, len(t_string1)):
        for j in range(1, len(t_string2)):
            solo_from_line1 = gap_penalty + s[i - 1][j]
            solo_from_line2 = gap_penalty + s[i][j - 1]
            pair_from_line1 = solo_from_line1 if i <= 1 else (
                    gap_2_penalty + s[i - 2][j] + pairing_cost(t_string1[i], t_string1[i - 1]))
            pair_from_line2 = solo_from_line2 if j <= 1 else (
                    gap_2_penalty + s[i][j - 2] + pairing_cost(t_string2[j], t_string2[j - 1]))
            current_pair = pairing_cost(t_string1[i], t_string2[j]) + s[i - 1][j - 1]

            s[i][j] = min(
                solo_from_line1,
                solo_from_line2,
                pair_from_line1,
                pair_from_line2,
                current_pair
            )

    print(s[len(string1)][len(string2)])

    return s[len(string1)][len(string2)], s


def main():
    """
    main driver function
    :return: None
    """
    # line1, line2 = process_dummy_input()
    line1, line2 = process_input()
    find_min_headache(line1, line2, 5, 4, 3)


if __name__ == '__main__':
    main()
