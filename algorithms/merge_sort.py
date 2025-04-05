from typing import List
from algorithms.algorithm import Algo
from algorithms.tools import timeit

class MergeSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Executes merge sort on the provided list of integers and returns the sorted list.
        Timing is handled by the decorator.
        """
        return self.merge_sort(arr)

    def merge_sort(self, arr: List[int]) -> List[int]:
        """
        Recursively divides the array and sorts it using the merge sort algorithm.
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])  # Recursively sort the left half
        right = self.merge_sort(arr[mid:])  # Recursively sort the right half

        # Merge the sorted halves and return the result
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        """
        Merges two sorted lists into a single sorted list.
        """
        sorted_arr = []
        i = j = 0

        # Compare elements from both halves and merge them in sorted order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        # Append any remaining elements from both halves
        sorted_arr += left[i:]
        sorted_arr += right[j:]

        return sorted_arr
