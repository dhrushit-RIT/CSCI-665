"""
    file: food.py
    description: determine if it would be possible to use all the donated food without any going to waste
    language: python3
    author: Dhrushit Raval - dr9703@g.rit.edu
    author: Julia Sanguinetti - js8848@rit.edu
"""


class Food:
    """
    Describes the food, with its arrival time and shelf life
    """
    __slots__ = "arrival_time", "shelf_life"

    def __init__(self, arrival_time, shelf_life):
        self.arrival_time = arrival_time
        self.shelf_life = shelf_life

    def get_effective_shelf_life(self, current_day):
        """
        determines the number of days the food will be fine from/after the current day
        :param current_day: current day
        :return: number of days after current day after which the food goes fowl
        """
        return self.shelf_life + self.arrival_time - current_day

    def __str__(self):
        return "({arrival}, {shelf})".format(arrival=str(self.arrival_time), shelf=str(self.shelf_life))


def process_input():
    """
    This function returns an array containing the list of food items.
    :param: None.
    :return: array of food items
    """
    num_food_items = int(input())
    food_list = []

    for food_item_index in range(num_food_items):
        food_details = input().strip().split()
        arrival_time = int(food_details[0])
        shelf_life = int(food_details[1])

        food_list.append(Food(arrival_time, shelf_life))

    return food_list


class Heap:
    """
    Defines a heap

    heap - the list that contains the heap items
    days_passed - current day for processing
    """
    __slots__ = "heap", "days_passed"

    def __init__(self):
        self.heap = []
        self.days_passed = 0

    def has_food(self):
        """
        determines if the heap contains any food items currently
        :return:
        """
        return len(self.heap)

    def set_day(self, days_passed):
        """
        sets the current day
        :param days_passed: the day to set the current day by
        :return:
        """
        self.days_passed = days_passed

    def next_day(self):
        """
        updates the current day to the next
        :return:
        """
        self.days_passed += 1

    def sift_down(self):
        """
        sift down process on the currently inserted food item at the root
        :return:
        """
        index = 0
        while index < len(self.heap):
            parent_shelf_life = self.heap[index].get_effective_shelf_life(self.days_passed)
            left_child_exists = False
            right_child_exists = False
            if len(self.heap) > 2 * index + 1:
                left_child_exists = True
                left_child_shelf_life = self.heap[(2 * index + 1)].get_effective_shelf_life(self.days_passed)
            if len(self.heap) > 2 * index + 2:
                right_child_exists = True
                right_child_shelf_life = self.heap[(2 * index + 2)].get_effective_shelf_life(self.days_passed)

            if (left_child_exists and parent_shelf_life > left_child_shelf_life) or (
                    right_child_exists and parent_shelf_life > right_child_shelf_life):
                temp = self.heap[index]
                if not right_child_exists or left_child_shelf_life < right_child_shelf_life:
                    self.heap[index] = self.heap[(2 * index + 1)]
                    index = 2 * index + 1
                else:
                    self.heap[index] = self.heap[(2 * index + 2)]
                    index = 2 * index + 2
                self.heap[index] = temp
            else:
                break

    def sift_up(self):
        """
        moves up the food item till its priority is more than the parent's
        :return:
        """
        index = len(self.heap) - 1
        while index > 0:
            child_shelf_life = self.heap[index].get_effective_shelf_life(self.days_passed)
            parent_shelf_life = self.heap[(index - 1) // 2].get_effective_shelf_life(self.days_passed)
            if child_shelf_life < parent_shelf_life:
                temp = self.heap[index]
                self.heap[index] = self.heap[(index - 1) // 2]
                self.heap[(index - 1) // 2] = temp
                index = (index - 1) // 2
            else:
                break

    def insert(self, food):
        """
        inserts food item into the heap
        :param food: food item to insert
        :return: None
        """
        self.heap.append(food)
        self.sift_up()

    def remove(self):
        """
        removes the food item at the root
        :return: food item at the root
        """
        ret_value = self.heap[0]
        last_food = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_food
            self.sift_down()

        return ret_value


def process_food(food_list):
    """
    use the most priority food item in the heap (food item at the root)
    :param food_list: list of food items to be processed
    :return: True - if all the food items can be used without wasting them
    False - if one of the food items goes fowl
    """
    food_heap = Heap()
    day = 0
    process_from = 0
    process_till = 0
    while True:
        while process_till < len(food_list) and food_list[process_till].arrival_time <= day:
            process_till += 1

        for index in range(process_from, process_till):
            food_heap.insert(food_list[index])

        # print("heap: ", *food_heap.heap)
        if food_heap.has_food():
            food_to_use = food_heap.remove()
            # print("food to use : ", food_to_use)
            if food_to_use.get_effective_shelf_life(day) <= 0:
                return False
        else:
            day = food_list[process_from].arrival_time - 1
            food_heap.set_day(day)

        food_heap.next_day()
        day += 1

        process_from = process_till

        if len(food_heap.heap) == 0:
            food_to_still_process = process_till < len(food_list)
            if not food_to_still_process:
                return True
            else:
                continue


def main():
    """
    Main driver function
    Prints true if the list of food items donated can be used without wasting them
    :return: None
    """
    food_list = process_input()
    # print("food list ready", food_list)
    used_all_food = process_food(food_list)
    if used_all_food:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
