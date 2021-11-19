"""
    file: sphere.py
    description: determine if there exists any sphere centered at the origin (0, 0, 0) having two or more of the n points on its surface
    language: python3
    author: Dhrushit Raval - dr9703@g.rit.edu
    author: Julia Sanguinetti - js8848@rit.edu
"""


class Point:
    """
        Describes a point in 3D
    """
    __slots__ = "x", "y", "z", "radius"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.radius = x ** 2 + y ** 2 + z ** 2

    def __str__(self):
        return "[({x}, {y}, {z})  {rad} ] ".format(x=str(self.x), y=str(self.y), z=str(self.z), rad=str(self.radius))


class RadixItem:
    """
        Wrapper to wrap the actual point and sort using Radix Sort
    """
    __slots__ = "next", "eff_num", "num_for_comp", "actual_item"

    def __init__(self, initial_num, item):
        self.eff_num = initial_num
        self.num_for_comp = 0
        self.next = None
        self.actual_item = item

    def setup_for_ittr(self):
        """
        determines the least significant digit to compare the number with

        params: None
        :return: None
        """
        self.num_for_comp = self.eff_num % 10
        self.eff_num //= 10
        self.next = None

    def __str__(self):
        return "{val}".format(val=str(self.actual_item))


class Radix:
    __slots__ = "item_list", "max_num", "sorted_list", "bucket_list"

    def get_iterations_needed(self, num):
        """
       determines the number of iterations needed for Radix Sort (the k value in O(n+k))
       Equal to the number of digits in the max number from the list

       params: None
       :return: None
       """
        num_ittr = 0
        while num > 0:
            num_ittr += 1
            num //= 10
        return num_ittr

    def __init__(self, items, radix=10):
        self.item_list = []
        self.sorted_list = []
        self.bucket_list = []
        self.max_num = 0

        for i in range(radix):
            self.bucket_list.append([])

        for (num, item) in items:
            self.item_list.append(RadixItem(num, item))

    def sort_radix(self):
        """
       sorts the items in the list using radix sort

       params: None
       :return: List of items sorted by current least significant digit
       """
        num_ittr = self.get_iterations_needed(max([x.eff_num for x in self.item_list]))

        for index in range(1, num_ittr + 1):
            for item in self.item_list:
                item.setup_for_ittr()
            for item in self.item_list:
                self.bucket_list[item.num_for_comp].append(item)

            self.sorted_list = []
            for i in range(len(self.bucket_list)):
                self.sorted_list.extend(self.bucket_list[i])
                self.bucket_list[i] = [] # empty the bucket after collecting the items

            self.item_list = self.sorted_list

        return [x.actual_item for x in self.item_list]


def process_input():
    """
    This function returns an array containing the points to sort.
    :param: None.
    :return: array of points based on input provided
    """
    num_inputs = int(input())

    points = []
    for index in range(num_inputs):
        point_details = input().strip().split()
        x, y, z = int(point_details[0]), int(point_details[1]), int(point_details[2])
        point = Point(x, y, z)
        points.append(point)

    return points


def radix_sort_points(points):
    """
    helper function to call radix sort on the array
    :param points:
    :return:
    """
    # print(*points)
    radix = Radix([(x.radius, x) for x in points])
    sorted_arr = radix.sort_radix()
    # print(*sorted_arr)
    return sorted_arr


def check_for_same_radius(points):
    """
    Checks if any two points in the list have the same radius
    :param points: list of points sorted by radius with origin as center of circle
    :return: YES - if there are two or more points with same radius
    NO - if there no two points have same radius
    """
    total_size = len(points)
    for i in range(total_size):
        if i + 1 < total_size:
            if points[i].radius == points[i + 1].radius:
                return True
    return False


def main():
    """
    main driver function
    :return:
    """
    points = process_input()
    sorted_points = radix_sort_points(points)
    if check_for_same_radius(sorted_points):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
