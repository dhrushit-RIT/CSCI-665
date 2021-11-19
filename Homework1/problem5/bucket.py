"""
file: bucket.py
description: Bucket class.
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""


class Bucket:
    __slots__ = 'blist'

    def __init__(self):
        self.blist = []
    """
    This function inserts provided value into bucket.
    :param: value to be inserted.
    :return:  
    """ 
    def insert(self, value):
        # print("inserting", value)
        if len(self.blist) == 0:
            self.blist.append(value)
        else:
            index = 0
            while index < len(self.blist) and self.blist[index] < value:
                index += 1
            self.blist.insert(index, value)
        
    def get_list(self):
        return self.blist
    
    """
    This function sorts the bucket in ascending order.
    :param: None.
    :return: None. 
    """ 
    def sort_list(self):
        self.blist.sort()
        # for i in range(1, len(self.blist), 1):
        #     # print("-----xxxxx-----xxxxx-----xxxxx-----xxxxx-----xxxxx-----")
        #     for j in range(i, 0, -1):
        #         if self.blist[j-1] > self.blist[j]:
        #             (self.blist[j-1], self.blist[j]) = (self.blist[j], self.blist[j-1])
        #         else:
        #             continue
        #         # print(self.blist)

        
