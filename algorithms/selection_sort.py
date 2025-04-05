from algorithm import Algo
from typing import List
from tools import timeit

class SelectionSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        n = len(arr)
        for i in range(n):
            minid =  i
            for j in range(i, n):
                if arr[j] < arr[minid]:
                    minid = j
            arr[i], arr[minid] = arr[minid], arr[i]
        return arr
