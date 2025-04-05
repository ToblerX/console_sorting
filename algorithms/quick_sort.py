from typing import List
from algorithm import Algo
from tools import timeit


class QuickSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        def sorting(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in  arr if x > pivot]
            return sorting(left) + mid + sorting(right)
        return sorting(arr)