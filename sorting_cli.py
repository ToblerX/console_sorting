import argparse
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
    return sorted_arr, time_taken


def compare_algorithms(arr, algo1, algo2):
    sorted_arr1, time1 = get_sorting_time(arr, algo1)
    sorted_arr2, time2 = get_sorting_time(arr, algo2)

    print(f"Sorting with {algo1}: {sorted_arr1}, Time taken: {time1:.6f} seconds")
    print(f"Sorting with {algo2}: {sorted_arr2}, Time taken: {time2:.6f} seconds")

    if sorted_arr1 == sorted_arr2:
        print("Both algorithms produced the same sorted result.")
    else:
        print("The sorting results differ between the algorithms.")


def post_algorithm_info(algorithm_name):
    info = {
        "QuickSort": "QuickSort: An efficient divide-and-conquer algorithm.",
        "BubbleSort": "BubbleSort: A simple comparison-based algorithm with poor performance for large lists.",
        "MergeSort": "MergeSort: A divide-and-conquer algorithm that splits and merges.",
        "InsertionSort": "InsertionSort: A simple sorting algorithm that builds the sorted list one item at a time.",
        "SelectionSort": "SelectionSort: An inefficient comparison-based algorithm.",
        "TimSort": "TimSort: A hybrid sorting algorithm derived from merge sort and insertion sort.",
        "RadixSort": "RadixSort: A non-comparative sorting algorithm based on digit-wise sorting.",
        "CountingSort": "CountingSort: A non-comparative sorting algorithm that counts occurrences of elements.",
        "BucketSort": "BucketSort: A sorting algorithm that divides elements into buckets and sorts each bucket."
    }
    return info.get(algorithm_name, "Unknown algorithm")


def main():
    parser = argparse.ArgumentParser(description="Sorting Algorithms CLI")
    parser.add_argument("-a", "--algorithm", type=str, required=True,
                        help="Algorithm name (e.g., QuickSort, BubbleSort, etc.)")
    parser.add_argument("-s", "--size", type=int, required=True, help="Size of the array to sort")
    parser.add_argument("-c", "--compare", type=str, nargs=2,
                        help="Compare two algorithms (e.g., QuickSort BubbleSort)")
    parser.add_argument("-p", "--post", type=str, help="Post information about an algorithm (e.g., QuickSort)")

    args = parser.parse_args()

    # Generate an array of random numbers of the specified size
    arr = [i for i in range(args.size, 0, -1)]  # Reverse ordered array for testing

    # Get sorting time for the selected algorithm
    if args.algorithm:
        sorted_arr, time_taken = get_sorting_time(arr, args.algorithm)
        print(f"Sorted Array using {args.algorithm}: {sorted_arr}")
        print(f"Time taken: {time_taken:.6f} seconds")
        print("-" * 50)

    # Compare two algorithms
    if args.compare:
        compare_algorithms(arr, args.compare[0], args.compare[1])

    # Post information about the selected algorithm
    if args.post:
        info = post_algorithm_info(args.post)
        print(info)


if __name__ == "__main__":
    main()
