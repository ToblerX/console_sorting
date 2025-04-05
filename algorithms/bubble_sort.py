from typing import List
from algorithms.algorithm import Algo
from tools import timeit


class BubbleSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Sorts the array using the bubble sort algorithm.
        The timing logic is handled by the decorator.
        """
        return self.bubble_sort(arr)

    def bubble_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts the provided list of integers using the bubble sort algorithm.
        This is an in-place sorting algorithm.
        """
        n = len(arr)
        for i in range(n):
            swapped = False  # Flag to track if any swaps happened during this pass
            for j in range(n - i - 1):  # Compare adjacent elements up to the unsorted part
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if elements are in wrong order
                    swapped = True

            # If no swaps were made, the array is already sorted, and we can break early
            if not swapped:
                break
        return arr
