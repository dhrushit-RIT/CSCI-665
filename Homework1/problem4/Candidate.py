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
