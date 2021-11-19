

'''
==========================================================================================
Candidate Class
'''

"""
file: Candidate.py
description: Candidate class methods.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""
class Candidate:
    __slots__ = 'name', 'preference_list', 'paired_index', 'is_paired', 'ask_index', 'paired_with', 'asked_list', 'to_ask'
    """
    The method is called when an object from class Candidate 
    is created and it initializes the attributes of such class.

    :param: None 
    :return: None
    """

    def __init__(self, name, preference_list):
        self.name = name
        self.paired_index = -1
        self.preference_list = preference_list
        self.to_ask = preference_list[:]
        self.asked_list = []
        self.is_paired = False
        self.paired_with = None

    """
    The function initializes all candidates to free.

    :param: None 
    :return: None
    """
    def reset(self):
        self.is_paired = False
        self.paired_index = -1
        self.paired_with = None
        self.ask_index = 0
        self.to_ask = self.preference_list[:]
        self.asked_list = []

    """
    The function pairs candidates from the given input.

    :param: None 
    :return: None
    """

    def pair(self, pair_with, pair_partner=False):
        if pair_partner == True:
            pair_with.pair(self)
        self.paired_with = pair_with
        self.is_paired = True
        self.paired_index = self.preference_list.index(pair_with.name)
    """
    The function unpairs candidates if better pairing found.

    :param: None 
    :return: None
    """
    def unpair(self, unpair_partner=False):
        if unpair_partner == True:
            self.paired_with.unpair()

        self.paired_with = None
        self.is_paired = False
    """
    The function updates the index position in the array.

    :param: None 
    :return: None
    """
    def update_next_ask_index(self):
        self.ask_index += 1
    """
    The function returns the next candidate to be asked for preference.

    :param: None 
    :return: next candidate to ask for matching.
    """
    def next_ask_candidate(self):
        # print("Asker preferenece: ", self.to_ask)
        next_to_ask = self.to_ask.pop(0)
        self.asked_list.append(next_to_ask)
        return next_to_ask
    """
    The function compares candidates preferences.

    :param: candidate 
    :return: True if candidate has a preference over current, False, otherwise.
    """
    def prefers(self, candidate):
        return self.preference_list.index(self.paired_with.name) > self.preference_list.index(candidate.name)


# from problem4.Candidate import Candidate
"""
file: matches.py
description: Determine if there exist two completely
different stable matchings for the given data.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""

# from Candidate import Candidate

"""
The function initializes all candidates to free. 

:param: group of candidates
:return: None
"""


def reset_pairing(group):
    for candidate in group:
        candidate.reset()


"""
This is the gale shapley algorithm to find 
stable matchings from the given data. It takes an equal 
number of candidates per group and their preferences from 
the input provided. 

:param: two groups of candidates to pair from input
:return: group pairings based on preferences
"""


def gale_shapley(group1, group2):
    reset_pairing(group1)
    reset_pairing(group2)
    pending_group1 = [x for x in group1]

    asker_group_map = {x.name: x for x in group1}
    asked_group_map = {x.name: x for x in group2}

    while len(pending_group1) > 0:
        # print([x.name for x in pending_group1])
        asker = pending_group1.pop(0)
        asked = asked_group_map[asker.next_ask_candidate()]

        if asked.is_paired == False:
            asked.pair(asker, True)
            # print(asker.name, "paired with", asked.name)

        elif asked.is_paired == True and asked.prefers(asker):

            unpairing_candidate = asker_group_map[asked.paired_with.name]
            pending_group1.insert(0, unpairing_candidate)

            unpairing_candidate.unpair(True)
            asked.pair(asker, True)

        else:
            pending_group1.insert(0, asker)
            continue

    return [(x.name, x.paired_with.name) for x in group1]


"""
This function processes the input containing the candidates
and their preferences by putting them in individual arrays.

:param: None
:return: two arrays containing the candidates preferences
 from each group
"""


def process_input():
    group_size = int(input())

    first_group = []
    second_group = []

    for i in range(group_size):
        preference_list = input()
        preference_list = preference_list.strip().split()
        preference_list = [int(x) for x in preference_list]

        first_group.append(Candidate(i, preference_list))

    for i in range(group_size):
        preference_list = input()
        preference_list = preference_list.strip().split()
        preference_list = [int(x) for x in preference_list]

        second_group.append(Candidate(i, preference_list))

    return (first_group, second_group)


"""
The main function calls gale_shapley function and applies it to
the arrays containing the candidates preferences. 
It then checks whether there are two completely different 
matchings and returns "YES" if that is the case or "NO" otherwise.

:param: None
:return: "YES" if there exist two completely different matchings. 
"NO" otherwise.
"""


def main():
    first_group, second_group = process_input()
    result1 = gale_shapley(first_group, second_group)
    result2 = gale_shapley(second_group, first_group)

    # to make the group1 items appear as the first element in the pair
    result2_inverted = []
    for t in result2:
        result2_inverted.append((t[1], t[0]))

    if len(list(set(result1) & set(result2_inverted))) > 0:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()




