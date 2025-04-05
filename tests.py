import random
from algorithms.bubble_sort import BubbleSort
from algorithms.selection_sort import SelectionSort
from algorithms.merge_sort import MergeSort
from algorithms.insertion_sort import InsertionSort
from algorithms.quick_sort import QuickSort
from algorithms.tim_sort import TimSort
from algorithms.radix_sort import RadixSort
from algorithms.counting_sort import CountingSort
from algorithms.bucket_sort import BucketSort
from typing import List


def generate_large_test_case(size: int) -> List[int]:
    """Generate a random list of integers of a given size."""
    return [random.randint(1, 10000) for _ in range(size)]


def main():
    # Testing with a smaller dataset
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

        # Testing with large datasets
        (generate_large_test_case(10000), "QuickSort"),
        (generate_large_test_case(10000), "BubbleSort"),
        (generate_large_test_case(10000), "MergeSort"),
        (generate_large_test_case(10000), "InsertionSort"),
        (generate_large_test_case(10000), "SelectionSort"),
        (generate_large_test_case(10000), "TimSort"),
        (generate_large_test_case(10000), "RadixSort"),
        (generate_large_test_case(10000), "CountingSort"),
        (generate_large_test_case(10000), "BucketSort"),
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

        # Run the algorithm and get both the sorted array and execution time
        sorted_arr, time_taken = sorter.run(arr, count_time=True)

        # Print the sorted array and time taken with formatted output
        print(f"Sorted Array using {algo_name}: {sorted_arr[:10]}...")  # Displaying first 10 elements for brevity
        if time_taken is not None:
            print(f"Execution Time: {time_taken:.6f} seconds")
        print("-" * 50)


if __name__ == '__main__':
    main()
