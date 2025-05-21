"""
Implementation of the Quick Sort algorithm.
Quick Sort is an in-place, divide-and-conquer sorting algorithm with average-case O(n log n) performance.
"""

def quick_sort(arr):
    """
    Sorts the input list using the quick sort algorithm.

    Args:
        arr (list): List of comparable elements to be sorted.

    Returns:
        list: The same list, sorted in-place.
    """
    def _quick_sort(items, low, high):
        if low < high:
            # Partition the list and get pivot index
            pivot_index = partition(items, low, high)

            # Recursively sort elements before and after partition
            _quick_sort(items, low, pivot_index - 1)
            _quick_sort(items, pivot_index + 1, high)

    def partition(items, low, high):
        """
        Partitions the list around the pivot (last element).
        Elements <= pivot go to the left; elements > pivot go to the right.

        Returns:
            int: Final index of the pivot
        """
        pivot = items[high]
        i = low - 1

        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]

        # Place pivot in correct position
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr
