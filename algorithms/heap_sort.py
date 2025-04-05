from typing import List
from algorithms.algorithm import Algo
from algorithms.tools import timeit


class HeapSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        """
        Executes heap sort on the provided list of integers and returns the sorted list.
        Uses a decorator to time the operation if count_time is True.
        """
        return self.heap_sort(arr)

    def heap_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts the list using the heap sort algorithm.
        """
        n = len(arr)

        # Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            self.heapify(arr, i, 0)  # Heapify the root of the reduced heap

        return arr

    def heapify(self, arr: List[int], n: int, i: int) -> None:
        """
        Maintains the heap property for the subtree rooted at index i.
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child is larger than root
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and heapify the affected subtree
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            self.heapify(arr, n, largest)  # Heapify the affected subtree
