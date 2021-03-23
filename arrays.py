#!/usr/bin/env python3

class BinarySearch:
    __my_list = []
    __value = None

    # TIME: log(n) == "logarithmic" because, at most, will check everything
    # # on either side (i.e. half list of previous iteration)
    # SPACE: 1 == "constant" because using input list, no extra space
    def get_index_recursively(self, my_list, value):
        if len(my_list) == 0:
            return -1
        
        self.__my_list = my_list
        self.__value = value

        return self.__recurse(0, len(self.__my_list) - 1)
    
    def __recurse(self, low_index, high_index):
        middle_index = (low_index + high_index) // 2
        middle_value = self.__my_list[middle_index]

        if self.__value == middle_value:
            return middle_index
        elif self.__value < middle_value and middle_index - 1 >= low_index:
            return self.__recurse(low_index, middle_index - 1)
        elif self.__value > middle_value and middle_index + 1 <= high_index:
            return self.__recurse(middle_index + 1, high_index)
        
        return -1