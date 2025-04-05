from algorithm import Algo
from typing import List, Tuple, Union
import time


class BubbleSort(Algo):
    def __init__(self, arr, count_time):
        super().__init__(arr, count_time)

    def run(self, arr: list, count_time: bool) -> Union[List[int], Tuple[List[int], float]]:
        if count_time:
            start = time.time()

        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

        if count_time:
            end = time.time()
            return arr, end - start
        return arr
