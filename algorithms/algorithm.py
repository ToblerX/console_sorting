from typing import List, Tuple, Optional

class Algo(object):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        self.arr = arr
        self.count_time = count_time

    def run(self, arr: List[int], count_time: bool) -> Tuple[List[int], Optional[float]]:
        """Sort the array using algorithm X, return (sorted list, time or None)"""
        pass