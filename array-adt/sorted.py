#!/usr/bin/env python3

class Sorted:
    def insert(self, my_list, value):
        """Insert value at sorted position, in sorted list.

        Args:
            my_list (int[]): List of sorted integers.
            value (int): Value to insert.

        Returns:
            int[]: Sorted list with value in sorted position.
        """

        index = len(my_list) - 2

        while index >= 0 and my_list[index] > value:
            my_list[index + 1] = my_list[index]
            index -= 1
        
        my_list[index + 1] = value

        return my_list
    
    def is_sorted(self, my_list):
        index = len(my_list) - 2
        while index >= 0 and my_list[index] < my_list[index + 1]:
            index -= 1
        
        return index == -1