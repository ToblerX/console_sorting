from typing import List, Tuple, Optional
from abc import ABC, abstractmethod

class Algo(ABC):
    def __init__(self, arr: List[int], count_time: bool) -> None:
        self.arr = arr
        self.count_time = count_time

    @abstractmethod
    def run(self, arr: List[int], count_time: bool) -> Tuple[List[int], Optional[float]]:
        pass
