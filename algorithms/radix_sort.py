from typing import List
from algorithms.algorithm import Algo
from algorithms.tools import timeit


class RadixSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Executes radix sort on the provided list of integers.
        Uses a decorator to time the operation if count_time is True.
        """
        return self.radix_sort(arr)

    def radix_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts the list using the radix sort algorithm by repeatedly applying counting sort
        on individual digit places (ones, tens, hundreds, etc.).
        """
        exp = 1  # Start with the least significant digit
        maxnum = max(arr)  # Get the maximum number to determine the number of digits

        # Perform counting sort for every digit (starting from least significant digit)
        while maxnum // exp > 0:
            self.counting_sort(arr, exp)
            exp *= 10  # Move to the next digit place (ones -> tens -> hundreds)

        return arr

    def counting_sort(self, arr: List[int], exp: int) -> None:
        """
        Performs counting sort on the given list based on the digit represented by `exp`.
        This function assumes that `exp` is the place value (e.g., ones, tens, hundreds, etc.).
        """
        n = len(arr)
        output = [0] * n  # Output array to store the sorted elements
        count = [0] * 10  # Count array to store the frequency of digits (0-9)

        # Store count of occurrences of (arr[i] // exp) % 10
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        # Change count[i] to contain the actual position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array by placing elements at their correct positions
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copy the output array to arr[], so that arr[] contains the sorted numbers
        for i in range(n):
            arr[i] = output[i]