from algorithm import Algo
from typing import List
from tools import timeit

class InsertionSort(Algo):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        super().__init__(arr, count_time)

    @timeit
    def run(self, arr: List[int], count_time: bool) -> List[int]:
        for i in range(len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and key<arr[j]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr