Sorting Algorithms CLI
======================

A command-line tool to run, compare, and learn about various sorting algorithms implemented in Python.

Features
--------
- Sort arrays using various popular algorithms.
- Compare performance of two sorting algorithms.
- Display theoretical information about each algorithm.
- Choose between randomly generated or reversed arrays for testing.

Implemented Algorithms
----------------------
- QuickSort
- MergeSort
- BubbleSort
- InsertionSort
- SelectionSort
- TimSort
- RadixSort
- CountingSort
- BucketSort
- HeapSort

Project Structure
-----------------
console_sorting/
│
├── algorithms/
│   ├── tools.py
│   ├── algorithm.py
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── merge_sort.py
│   ├── insertion_sort.py
│   ├── quick_sort.py
│   ├── tim_sort.py
│   ├── radix_sort.py
│   ├── counting_sort.py
│   ├── bucket_sort.py
│   └── heap_sort.py
│
├── sorting_cli.py
└── README.txt

Getting Started
---------------
1. Clone the Repository:

    git clone https://github.com/ToblerX/sorting-cli.git
    cd sorting-cli

2. Run the Script:

    python sorting_cli.py [OPTIONS]

Options
-------
  -a, --algorithm   Name of the sorting algorithm to run (e.g., QuickSort, MergeSort, etc.)
  -s, --size        Size of the array to sort
  -c, --compare     Compare two algorithms (e.g., -c QuickSort MergeSort)
  -p, --post        Show theoretical information about the algorithm
  -d, --data        Type of data to sort: random or reversed (default: reversed)

Note: --algorithm is not required when using --compare.

Examples
--------
Run a specific algorithm:

    python sorting_cli.py -a QuickSort -s 1000 -d random

Compare two algorithms:

    python sorting_cli.py -c QuickSort MergeSort -s 1000 -d random

Show theoretical information:

    python sorting_cli.py -a HeapSort -p

Requirements
------------
- Python 3.7+
- No external libraries needed

License
-------
This project is open source and available under the MIT License.

Happy sorting! ⚡
