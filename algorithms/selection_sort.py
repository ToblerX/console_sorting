from algorithm import Algo
from typing import List, Tuple, Union
import time

class SelectionSort(Algo):
    def __init__(self, arr, count_time):
        super().__init__(arr, count_time)

    def run(self, arr: list, count_time: bool) -> Union[List[int], Tuple[List[int], float]]:
        if count_time:
            start = time.time()

        #xxx

        if count_time:
            end = time.time()
            return arr, end - start
        return arr