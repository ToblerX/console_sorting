import time
from typing import Callable, Tuple, List, Optional
from functools import wraps

def timeit(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, arr: List[int], count_time: bool) -> Tuple[List[int], Optional[float]]:
        if count_time:
            start = time.time()
            result = method(self, arr, count_time)
            end = time.time()
            return result, end - start
        else:
            result = method(self, arr, count_time)
            return result, None
    return wrapper
