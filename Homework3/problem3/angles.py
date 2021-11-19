"""
file: angles.py
description: Determines the number of right triangles
that can formed by choosing sets of three points
language: python3
author: Dhrushit Raval - dr9703@g.rit.edu
author: Julia Sanguinetti - js8848@rit.edu
"""

class Point:
    __slots__ = "x", "y"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{x: " + str(self.x) + ", y: " + str(self.y) + "}"


class Line:
    __slots__ = "point1", "point2", "delX", "delY", "slope", "slope_sign", "length"

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
        self.delX = point2.x - point1.x
        self.delY = point2.y - point1.y
        if self.delX != 0:
            self.slope = self.delY / self.delX
        else:
            self.slope = None
        self.slope_sign = self.delY * self.delX
        if self.slope_sign >= 0:
            self.slope_sign = 1
        else:
            self.slope_sign = -1

        if self.delX < 0:
            self.delX *= -1
            self.delY *= -1
        self.length = self.delY * self.delY + self.delX * self.delX

    # def __cmp__(self, other):
    #     return self.delX * other.delY - self.delY * other.delX < 0

    def __lt__(self, other):
        return self.delX * other.delY - self.delY * other.delX > 0

    def __gt__(self, other):
        return self.delX * other.delY - self.delY * other.delX < 0

    def __le__(self, other):
        return self.delX * other.delY - self.delY * other.delX >= 0

    def __ge__(self, other):
        return self.delX * other.delY - self.delY * other.delX <= 0

    def __eq__(self, other):
        return self.delX * other.delY - self.delY * other.delX == 0

    def __ne__(self, other):
        return self.delX * other.delY - self.delY * other.delX != 0

"""
The function process input provided and returns array 
containing points with x, y coordinates
:param: None
:return: points with x,y coordinates based on input provided
"""

def process_input():
    n = int(input())
    points = []
    for _ in range(n):
        point = [int(x) for x in input().strip().split()]
        points.append(Point(point[0], point[1]))

    return points


def sort_dy(m: Line):
    return m.delY

def sort_dx(m: Line):
    return m.delX

"""
The function verifies whether two lines are perpendicular
 to each other by checking if the product of their slopes is less than 0
:param: two lines.
:return: True if the product of their slopes is less than 0. False otherwise.
"""
def line_comparator(line1: Line, line2: Line):
    return line1.delX * line2.delY - line2.delX * line2.delY < 0

"""
The function returns the total amount of right triangles
formed from given input.
:param: array containing the points based on input.
:return: number of right triangles formed from given input.
"""
def find_right_angles(points):
    right_angles_count = 0
    for p_focus_index in range(len(points)):
        lines = []
        for other_point_index in range(len(points)):  # n^2
            if p_focus_index == other_point_index:
                continue
            else:
                lines.append(Line(points[p_focus_index], points[other_point_index]))

        # using internal sort function - O(n log(n)) = n^2 logn
        # lines.sort(key=sort_dy)  # O(nlogn)
        # lines.sort(reverse=True, key=sort_dx)  # O(nlogn) = n^2 logn

        zero_slope_lines = [line for line in lines if line.slope == 0]
        infinite_slope_lines = [line for line in lines if line.slope is None]
        positive_slope_lines = [line for line in lines if (line.slope is not None and line.slope > 0)]
        negative_slope_lines = [line for line in lines if (line.slope is not None and line.slope < 0)]

        # O(n log n)

        right_angles_count += len(zero_slope_lines) * len(infinite_slope_lines)

        if len(positive_slope_lines) == 0 or len(negative_slope_lines) == 0:
            continue

        positive_slope_lines = sorted(positive_slope_lines) # O(n log n)
        negative_slope_lines = sorted(negative_slope_lines) # O(n log n)

        # normal_lines = [line for line in lines if (line.slope is not None and line.slope != 0)]

        negative_slope_index = 0
        negative_slope_iterator_index = 0
        positive_slope_index = 0
        positive_slope_iterator_index = 0

        while negative_slope_index < len(negative_slope_lines) and positive_slope_index < len(positive_slope_lines):

            line1: Line = positive_slope_lines[positive_slope_index]
            line2: Line = negative_slope_lines[negative_slope_index]

            slope_sum = line1.delY * line2.delY + line1.delX * line2.delX
            if slope_sum < 0:
                negative_slope_index += 1
                continue

            if slope_sum > 0:
                positive_slope_index += 1
                continue

            # handle the =0 scenario
            positive_slope_iterator_index = positive_slope_index
            negative_slope_iterator_index = negative_slope_index

            while positive_slope_iterator_index < len(positive_slope_lines):
                line1 = positive_slope_lines[positive_slope_iterator_index]
                line2 = negative_slope_lines[negative_slope_index]

                slope_sum = line1.delY * line2.delY + line1.delX * line2.delX
                if slope_sum != 0:
                    break
                positive_slope_iterator_index += 1

            while negative_slope_iterator_index < len(negative_slope_lines):
                line1 = positive_slope_lines[positive_slope_index]
                line2 = negative_slope_lines[negative_slope_iterator_index]

                slope_sum = line1.delY * line2.delY + line1.delX * line2.delX
                if slope_sum != 0:
                    break
                negative_slope_iterator_index += 1

            right_angles_count += (positive_slope_iterator_index - positive_slope_index) * (
                    negative_slope_iterator_index - negative_slope_index)
            positive_slope_index = positive_slope_iterator_index
            negative_slope_index = negative_slope_iterator_index

    return right_angles_count


def main():
    points = process_input()
    print(find_right_angles(points))


if __name__ == '__main__':
    main()
