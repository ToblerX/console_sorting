from typing import List
from algorithm import Algo
from tools import timeit

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

        # Choosing the pivot (here, we use the first element)
        pivot = arr[0]

        # Dividing the array into three subarrays: left, mid, and right
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recursively sorting and combining the subarrays
        return self.quick_sort(left) + mid + self.quick_sort(right)
