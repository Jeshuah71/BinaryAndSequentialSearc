import random
import statistics
import time
import matplotlib.pyplot as plt
from Algo_and_Struts_05_a_sequential_search import sequential_search


def binary_search(a_list, item):
    """Performs a binary search on a sorted list."""
    first = 0
    last = len(a_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False
