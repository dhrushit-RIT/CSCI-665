"""
    file: sphere.py
    description: computes the number of participants whose patience is lost before the parade starts
    language: python3
    author: Dhrushit Raval - dr9703@g.rit.edu
    author: Julia Sanguinetti - js8848@rit.edu
"""


class Participant:
    """
    Descrives a participant

    slots:
        patience - the patience that the participant has
        desired_location -  the location that the participant desires to stand at
    """
    __slots__ = "patience", "desired_location"

    def __init__(self, patience, desired_location):
        self.patience = patience
        self.desired_location = desired_location

    def __str__(self):
        return "({loc},{patience})".format(loc=self.desired_location, patience=self.patience)


def count_inversions(arr, tabs=0) -> [Participant]:
    """
    runs the count inversion algorithm using merge sort piggy backing
    :param arr: array of participants
    :return: List of participants sorted in the ascending order of their desired location
    """
    if len(arr) == 1:
        return arr

    mid_index = len(arr) // 2

    left_array = count_inversions(arr[:mid_index])
    right_array = count_inversions(arr[mid_index:])

    return_data = []
    left_array_index = 0
    right_array_index = 0

    left_patience_reduction = 0
    while left_array_index < len(left_array) and right_array_index < len(right_array):
        if left_array[left_array_index].desired_location <= right_array[right_array_index].desired_location:
            left_array[left_array_index].patience -= left_patience_reduction
            return_data.append(left_array[left_array_index])
            left_array_index += 1
        else:
            return_data.append(right_array[right_array_index])
            right_array[right_array_index].patience -= (len(left_array) - left_array_index)
            left_patience_reduction += 1

            right_array_index += 1

    if left_array_index < len(left_array):
        for participant in left_array[left_array_index:]:
            participant.patience -= left_patience_reduction
        return_data.extend(left_array[left_array_index:])

    if right_array_index < len(right_array):
        return_data.extend(right_array[right_array_index:])

    return return_data


def process_input() -> [Participant]:
    """
    creates Participants from input
    :return: list of participants
    """

    num_inputs = int(input())
    participants_list = []
    for index in range(num_inputs):
        participant_details = input().strip().split()
        desired_location = int(participant_details[0])
        patience = int(participant_details[1])

        participants_list.append(Participant(patience, desired_location))

    return participants_list


def how_many_lost_patience(participants):
    """
    returns the number of participants who lost the patience
    :param participants: list of participants
    :return: number of participants who lost the patience
    """

    num_lost_patience = 0

    for participant in participants:
        if participant.patience < 0:
            num_lost_patience += 1

    return num_lost_patience


def main():
    """
    main driving function
    prints count of the number of participants that lose the patience before the parade starts
    :return: None
    """
    participants = process_input()
    count_inversions(participants)
    print(str(how_many_lost_patience(participants)))


if __name__ == '__main__':
    main()
