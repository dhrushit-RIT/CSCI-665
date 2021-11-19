"""
    file: jobs.py
    description: Determines the max number of work the employee can do while switching between the employers.
    language: python3
    author: Dhrushit Raval - dr9703@g.rit.edu
    author: Julia Sanguinetti - js8848@rit.edu
"""

import copy


def process_input():
    """
    n = number of intervals
    n lines with start_time, end_time, employer_id
    :return: array
    """
    num_input = int(input())

    e1_jobs = []
    e2_jobs = []

    for i in range(num_input):
        interval_details = [int(x) for x in input().strip().split()]
        if interval_details[2] == 0:
            e1_jobs.append(Interval(interval_details[0], interval_details[1]))
        else:
            e2_jobs.append(Interval(interval_details[0], interval_details[1]))

    return e1_jobs, e2_jobs


def process_dummy_input():
    """
    for testing purposes only
    :return:
    """
    # input 1.1
    # e1 = [
    #     Interval(1, 4),
    #     Interval(2, 7),
    #     Interval(4, 8),
    #     Interval(8, 9),
    # ]
    # e2 = [
    #     Interval(2, 8),
    #     Interval(3, 5),
    #     Interval(10, 12),
    #     Interval(4, 6),
    # ]

    # input 1.2
    e1 = [Interval(10, 15),
          Interval(2, 4),
          Interval(8, 12),
          Interval(12, 18),
          Interval(4, 6),
          Interval(6, 9)]

    e2 = [Interval(9, 14),
          Interval(1, 3),
          Interval(3, 5),
          Interval(11, 17),
          Interval(5, 8),
          Interval(7, 11)]
    return e1, e2


class Interval:
    """
    Class to club the properties of an Interval
    """
    __slots__ = "start_time", "finish_time"

    def __init__(self, start_time, finish_time):
        self.start_time = start_time
        self.finish_time = finish_time

        assert start_time <= finish_time, "start time can not be less than end time"

    def __str__(self):
        return "{ " + str(self.start_time) + ", " + str(self.finish_time) + " }"

    def __lt__(self, other):
        return self.finish_time < other.finish_time

    def __gt__(self, other):
        return self.finish_time > other.finish_time

    def __le__(self, other):
        return self.finish_time <= other.finish_time

    def __ge__(self, other):
        return self.finish_time >= other.finish_time

    def __eq__(self, other):
        return self.finish_time == other.finish_time

    def __ne__(self, other):
        return self.finish_time != other.finish_time


def find_max_jobs(e1_jobs, e2_jobs):
    """
    finds the max number of jobs that the employee can do while switching between the two employers
    :param e1_jobs: the job intervals provided by employer 1
    :param e2_jobs: the job intervals provided by employer 2
    :return: max number of jobs that the employee can do while switching between the two employers
    """
    e1_jobs.sort()
    e2_jobs.sort()

    selected = []
    last_selected_from = None

    while True:

        if last_selected_from is None or last_selected_from == 1:
            if len(e1_jobs) == 0:
                break
            job = e1_jobs.pop(0)
            if len(selected) > 0 and job.start_time < selected[-1].finish_time:
                continue
            selected.append(job)
            last_selected_from = 0
        else:
            if len(e2_jobs) == 0:
                break
            job = e2_jobs.pop(0)
            if len(selected) > 0 and job.start_time < selected[-1].finish_time:
                continue
            selected.append(job)
            last_selected_from = 1
        # selected_job = selected[-1]

        #
        # remove jobs that start before the selected job ends
        #
        # e1_jobs = [job for job in e1_jobs if job.start_time >= selected_job.finish_time]
        # e2_jobs = [job for job in e2_jobs if job.start_time >= selected_job.finish_time]

    return selected


def main():
    """
    main driver function
    :return:
    """
    # e1_jobs, e2_jobs = process_dummy_input()
    e1_jobs, e2_jobs = process_input()
    e1_jobs_copy, e2_jobs_copy = copy.deepcopy(e1_jobs), copy.deepcopy(e2_jobs)  # O(n)
    array_to_process = []
    if e1_jobs is None or e2_jobs is None:
        print("only one employer has jobs")
        return
    max_jobs_1 = find_max_jobs(e1_jobs, e2_jobs)
    max_jobs_2 = find_max_jobs(e2_jobs_copy, e1_jobs_copy)
    print(max(len(max_jobs_1), len(max_jobs_2)))


if __name__ == '__main__':
    main()
