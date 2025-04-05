import random
from typing import List
from algorithms.algorithm import Algo
from algorithms.tools import timeit

class QuickSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Executes quicksort on the provided list of integers and returns the sorted list.
        The timing logic is handled by the decorator.
        """
        return self.quick_sort(arr)

    def quick_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts the list using the quicksort algorithm.
        """
        if len(arr) <= 1:
            return arr
        if len(arr) < 10:  # For small arrays, use InsertionSort (or any other small-array optimization)
            return self.insertion_sort(arr)

        # Choosing a random pivot
        pivot = random.choice(arr)

        # Dividing the array into three subarrays: left, mid, and right
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recursively sorting and combining the subarrays
        return self.quick_sort(left) + mid + self.quick_sort(right)

    def insertion_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts the list using Insertion Sort for small subarrays.
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
