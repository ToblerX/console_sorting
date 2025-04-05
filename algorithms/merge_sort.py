from typing import List, Tuple
from algorithm import Algo
from tools import timeit


class MergeSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left: List[int], right: List[int]) -> List[int]:
            sorted_arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
            sorted_arr += left[i:]
            sorted_arr += right[j:]
            return sorted_arr

        return merge_sort(arr)