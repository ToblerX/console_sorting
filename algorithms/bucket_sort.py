from typing import List
from algorithms.algorithm import Algo
from algorithms.tools import timeit


class BucketSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Executes bucket sort on the provided list of integers.
        Uses a decorator to time the operation if count_time is True.
        """
        return self.bucket_sort(arr)

    def bucket_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts the list using the bucket sort algorithm.
        Assumes the values are between 0 and 1 for simplicity,
        or handles scaling to work with a general range.
        """
        if len(arr) == 0:
            return arr  # No need to sort if the list is empty

        # Find the min and max values to scale the bucket index correctly
        min_value = min(arr)
        max_value = max(arr)

        # Initialize buckets (buckets are lists)
        n = len(arr)
        buckets = [[] for _ in range(n)]

        # Place each number in the corresponding bucket
        for num in arr:
            # Scale the number based on min/max values
            index = int((num - min_value) / (max_value - min_value) * (n - 1))
            buckets[index].append(num)

        # Sort individual buckets
        for bucket in buckets:
            bucket.sort()

        # Concatenate all sorted buckets into the final sorted array
        return [num for bucket in buckets for num in bucket]