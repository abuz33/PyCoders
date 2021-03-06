
from time import time


def bubbleSort(arr):  # compare and swap two adjacent items until all sorted: sorted part will gather at the end
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selectionSort(arr):  # select the minimum from the remaining
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertionSort(arr):  # insert the unsorted next element to the sorted part
    n = len(arr)

    # Traverse through 1 to n
    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def merge(arr, left_index, middle_index, right_index):
    """
    Merges two subarrays of arr[].
    - First subarray is arr[l..m]
    - Second subarray is arr[m+1..r]
    """
    n1 = middle_index - left_index + 1
    n2 = right_index - middle_index

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left_index + i]

    for j in range(0, n2):
        R[j] = arr[middle_index + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0               # Initial index of first subarray
    j = 0               # Initial index of second subarray
    k = left_index      # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# divide until non-divisible point then sort while merging
def mergeSort(arr, left_index, right_index):
    if left_index < right_index:

        # Same as (left_index+right_index)//2, but avoids overflow
        middle_index = (left_index+(right_index-1))//2

        # Sort first and second halves
        mergeSort(arr, left_index, middle_index)
        mergeSort(arr, middle_index+1, right_index)
        merge(arr, left_index, middle_index, right_index)


def partition(arr, low, high):
    """
     This function takes last element as pivot, places
     the pivot element at its correct position in sorted
     array, and places all smaller (smaller than pivot)
     to left of pivot and all greater elements to right
     of pivot
    """
    i = (low-1)           # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    """
    The main function that implements QuickSort
    arr[] - -> Array to be sorted,
    low - -> Starting index,
    high - -> Ending index
    """
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i-1]

    # Build the output array
    i = n-1
    while i >= 0:
        index = (arr[i]/exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr, exp)
        exp *= 10


arr = [10, 24, 56, 0, 45, 100]

start = time()
radixSort(arr)
print(arr)
end = time()
print("time: {}", end-start)
