from algorithms.bubble_sort import BubbleSort
from algorithms.selection_sort import SelectionSort
from algorithms.merge_sort import MergeSort
from algorithms.insertion_sort import InsertionSort
from algorithms.quick_sort import QuickSort
from algorithms.tim_sort import TimSort
from algorithms.radix_sort import RadixSort
from algorithms.counting_sort import CountingSort
from algorithms.bucket_sort import BucketSort


def main():
    test_cases = [
        ([170, 45, 75, 90, 802, 24, 2, 66], "QuickSort"),
        ([170, 45, 75, 90, 802, 24, 2, 66], "BubbleSort"),
        ([170, 45, 75, 90, 802, 24, 2, 66], "MergeSort"),
        ([170, 45, 75, 90, 802, 24, 2, 66], "InsertionSort"),
        ([170, 45, 75, 90, 802, 24, 2, 66], "SelectionSort"),
        ([170, 45, 75, 90, 802, 24, 2, 66], "TimSort"),
        ([170, 45, 75, 90, 802, 24, 2, 66], "RadixSort"),
        ([170, 45, 75, 90, 802, 24, 2, 66], "CountingSort"),
        ([170, 45, 75, 90, 802, 24, 2, 66], "BucketSort"),
    ]

    # Running each sorting algorithm on the test cases
    for arr, algo_name in test_cases:
        print(f"Testing {algo_name}...")
        if algo_name == "QuickSort":
            sorter = QuickSort(arr, count_time=True)
        elif algo_name == "BubbleSort":
            sorter = BubbleSort(arr, count_time=True)
        elif algo_name == "MergeSort":
            sorter = MergeSort(arr, count_time=True)
        elif algo_name == "InsertionSort":
            sorter = InsertionSort(arr, count_time=True)
        elif algo_name == "SelectionSort":
            sorter = SelectionSort(arr, count_time=True)
        elif algo_name == "TimSort":
            sorter = TimSort(arr, count_time=True)
        elif algo_name == "RadixSort":
            sorter = RadixSort(arr, count_time=True)
        elif algo_name == "CountingSort":
            sorter = CountingSort(arr, count_time=True)
        elif algo_name == "BucketSort":
            sorter = BucketSort(arr, count_time=True)

        # Run the algorithm
        sorted_arr = sorter.run(arr, count_time=True)

        # Print the sorted array
        print(f"Sorted Array using {algo_name}: {sorted_arr}")
        print("-" * 50)


if __name__ == '__main__':
    main()