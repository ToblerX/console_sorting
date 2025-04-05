from typing import List
from algorithm import Algo
from tools import timeit


class CountingSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Executes counting sort on the provided list of integers.
        Uses a decorator to time the operation if count_time is True.
        """
        return self.counting_sort(arr)

    def counting_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts the list using the counting sort algorithm.
        This algorithm works for both positive and negative integers.
        """
        n = len(arr)
        if n == 0:
            return arr  # No need to sort if the list is empty

        min_value = min(arr)
        max_value = max(arr)
        range_of_elems = max_value - min_value + 1

        # Initialize count array to store frequency of each number
        count = [0] * range_of_elems

        # Fill the count array with frequencies
        for num in arr:
            count[num - min_value] += 1

        # Modify count array to store cumulative counts
        for i in range(1, range_of_elems):
            count[i] += count[i - 1]

        # Build the output array
        output = [0] * n
        for i in range(n - 1, -1, -1):  # Process elements in reverse order
            num = arr[i]
            output[count[num - min_value] - 1] = num
            count[num - min_value] -= 1

        # Copy the sorted elements back into the original array
        for i in range(n):
            arr[i] = output[i]

        return arr
