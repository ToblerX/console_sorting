from algorithm import Algo
from typing import List
from tools import timeit

class BubbleSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
