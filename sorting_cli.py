import argparse
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


def get_sorting_time(arr, algorithm_name):
    sorter = None
    if algorithm_name == "QuickSort":
        sorter = QuickSort(arr, count_time=True)
    elif algorithm_name == "BubbleSort":
        sorter = BubbleSort(arr, count_time=True)
    elif algorithm_name == "MergeSort":
        sorter = MergeSort(arr, count_time=True)
    elif algorithm_name == "InsertionSort":
        sorter = InsertionSort(arr, count_time=True)
    elif algorithm_name == "SelectionSort":
        sorter = SelectionSort(arr, count_time=True)
    elif algorithm_name == "TimSort":
        sorter = TimSort(arr, count_time=True)
    elif algorithm_name == "RadixSort":
        sorter = RadixSort(arr, count_time=True)
    elif algorithm_name == "CountingSort":
        sorter = CountingSort(arr, count_time=True)
    elif algorithm_name == "BucketSort":
        sorter = BucketSort(arr, count_time=True)

    sorted_arr, time_taken = sorter.run(arr, count_time=True)
    return time_taken


def compare_algorithms(arr, algo1, algo2):
    time1 = get_sorting_time(arr, algo1)
    time2 = get_sorting_time(arr, algo2)

    print(f"Sorting with {algo1}, Time taken: {time1:.6f} seconds")
    print(f"Sorting with {algo2}, Time taken: {time2:.6f} seconds")

    if time1 < time2:
        print(f"{algo1} was faster by {time2 - time1:.6f} seconds")
    elif time2 < time1:
        print(f"{algo2} was faster by {time1 - time2:.6f} seconds")
    else:
        print("Both algorithms took the same time.")


def post_algorithm_info(algorithm_name):
    info = {
        "QuickSort": """
QuickSort:
    Description: QuickSort is a divide-and-conquer algorithm that selects a pivot element and sorts the array recursively.
    Time Complexity:
        Best: O(n log n)
        Average: O(n log n)
        Worst: O(n^2)
    Space Complexity: O(log n)
    Stable: No
    In-place: Yes
""",
        "BubbleSort": """
BubbleSort:
    Description: BubbleSort is a simple comparison-based algorithm with poor performance for large lists.
    Time Complexity:
        Best: O(n)
        Average: O(n^2)
        Worst: O(n^2)
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes
""",
        "MergeSort": """
MergeSort:
    Description: MergeSort is a divide-and-conquer algorithm that splits and merges the array.
    Time Complexity:
        Best: O(n log n)
        Average: O(n log n)
        Worst: O(n log n)
    Space Complexity: O(n)
    Stable: Yes
    In-place: No
""",
        "InsertionSort": """
InsertionSort:
    Description: InsertionSort is a simple sorting algorithm that builds the sorted array one element at a time.
    Time Complexity:
        Best: O(n)
        Average: O(n^2)
        Worst: O(n^2)
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes
""",
        "SelectionSort": """
SelectionSort:
    Description: SelectionSort is an inefficient comparison-based algorithm that repeatedly selects the smallest element.
    Time Complexity:
        Best: O(n^2)
        Average: O(n^2)
        Worst: O(n^2)
    Space Complexity: O(1)
    Stable: No
    In-place: Yes
""",
        "TimSort": """
TimSort:
    Description: TimSort is a hybrid sorting algorithm derived from merge sort and insertion sort.
    Time Complexity:
        Best: O(n)
        Average: O(n log n)
        Worst: O(n log n)
    Space Complexity: O(n)
    Stable: Yes
    In-place: No
""",
        "RadixSort": """
RadixSort:
    Description: RadixSort is a non-comparative sorting algorithm based on digit-wise sorting.
    Time Complexity:
        Best: O(nk)
        Average: O(nk)
        Worst: O(nk)
    Space Complexity: O(n)
    Stable: Yes
    In-place: No
""",
        "CountingSort": """
CountingSort:
    Description: CountingSort is a non-comparative sorting algorithm that counts the occurrences of elements.
    Time Complexity:
        Best: O(n + k)
        Average: O(n + k)
        Worst: O(n + k)
    Space Complexity: O(k)
    Stable: Yes
    In-place: No
""",
        "BucketSort": """
BucketSort:
    Description: BucketSort is a sorting algorithm that divides elements into buckets and sorts each bucket.
    Time Complexity:
        Best: O(n + k)
        Average: O(n + k)
        Worst: O(n^2)
    Space Complexity: O(n)
    Stable: Yes
    In-place: No
"""
    }
    return info.get(algorithm_name, "Unknown algorithm")


def generate_array(size, array_type="reversed"):
    if array_type == "random":
        return random.sample(range(size * 10), size)
    elif array_type == "reversed":
        return [i for i in range(size, 0, -1)]  # Reverse ordered array for testing
    else:
        raise ValueError("Unknown array type. Choose 'random' or 'reversed'.")


def main():
    parser = argparse.ArgumentParser(description="Sorting Algorithms CLI")
    parser.add_argument("-a", "--algorithm", type=str, required=True,
                        help="Algorithm name (e.g., QuickSort, BubbleSort, etc.)")
    parser.add_argument("-s", "--size", type=int, help="Size of the array to sort")
    parser.add_argument("-c", "--compare", type=str, nargs=2,
                        help="Compare two algorithms (e.g., QuickSort BubbleSort)")
    parser.add_argument('-p', '--post', action='store_true', help="Post information about the selected algorithm")
    parser.add_argument('-d', '--data', type=str, choices=["random", "reversed"], default="reversed",
                        help="Choose the array type: 'random' or 'reversed' (default: 'reversed')")

    args = parser.parse_args()

    # If -p is used, size argument is optional, but if -p isn't used, size is required
    if not args.post and not args.size:
        parser.error("The '-s/--size' argument is required unless '-p' is used.")

    # Generate the array based on the selected data type
    arr = generate_array(args.size, args.data) if args.size else []

    # Get sorting time for the selected algorithm
    if args.algorithm and not args.post:
        time_taken = get_sorting_time(arr, args.algorithm)
        print(f"Time taken by {args.algorithm}: {time_taken:.6f} seconds")
        print("-" * 50)

    # Compare two algorithms
    if args.compare:
        compare_algorithms(arr, args.compare[0], args.compare[1])

    # Post information about the selected algorithm
    if args.post:
        info = post_algorithm_info(args.algorithm)
        print(info)


if __name__ == "__main__":
    main()
