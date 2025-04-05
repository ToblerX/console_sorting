from typing import List
from algorithms.algorithm import Algo
from algorithms.tools import timeit


class TimSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Executes TimSort on the provided list of integers.
        Uses a decorator to time the operation if count_time is True.
        """
        return self.tim_sort(arr)

    def insertion_sort(self, arr: List[int], left: int, right: int) -> None:
        """Performs an insertion sort on the specified subarray of arr."""
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(self, arr: List[int], l: int, m: int, r: int) -> None:
        """Merges two sorted subarrays arr[l..m] and arr[m+1..r]."""
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]
        i = j = 0
        for k in range(l, r + 1):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

    def tim_sort(self, arr: List[int]) -> List[int]:
        """Sorts the list using the TimSort algorithm."""
        n = len(arr)
        RUN = 32

        # Sort individual subarrays of size RUN using insertion sort
        for i in range(0, n, RUN):
            self.insertion_sort(arr, i, min(i + RUN - 1, n - 1))

        # Merge sorted subarrays
        size = RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(left + size - 1, n - 1)
                right = min((left + 2 * size - 1), n - 1)
                if mid < right:
                    self.merge(arr, left, mid, right)
            size *= 2

        return arr
