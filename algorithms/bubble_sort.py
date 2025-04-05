from algorithm import Algo

class BubbleSort(Algo):
    def __init__(self, arr, count_time):
        super().__init__(arr, count_time)
    def run(self, arr: list, count_time: bool):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr #implement a timer and also return elapsed time if count_time=True