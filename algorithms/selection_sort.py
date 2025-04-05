from typing import List
from algorithm import Algo
from tools import timeit


class SelectionSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Sorts the array using the selection sort algorithm.
        The timing logic is handled by the decorator.
        """
        return self.selection_sort(arr)

    def selection_sort(self, arr: List[int]) -> List[int]:
        """
        Performs selection sort on the provided list of integers.
        This is an in-place sorting algorithm.
        """
        n = len(arr)

        for i in range(n):
            # Assume the current element is the minimum
            min_idx = i

            # Find the index of the minimum element in the unsorted portion
            for j in range(i + 1, n):  # We start from i+1 to avoid unnecessary comparison
                if arr[j] < arr[min_idx]:
                    min_idx = j

            # Swap the found minimum element with the element at the current position
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr
