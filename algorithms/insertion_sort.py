from typing import List
from algorithms.algorithm import Algo
from algorithms.tools import timeit


class InsertionSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Sorts the array using the insertion sort algorithm.
        The timing logic is handled by the decorator.
        """
        return self.insertion_sort(arr)

    def insertion_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts the provided list of integers using the insertion sort algorithm.
        This is an in-place sorting algorithm.
        """
        # Iterate through each element in the array starting from the second element
        for i in range(1, len(arr)):
            key = arr[i]  # The current element to insert
            j = i - 1  # Start comparing with the element just before the current element

            # Shift elements that are greater than key to one position ahead
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            # Place the key at its correct position
            arr[j + 1] = key

        return arr
