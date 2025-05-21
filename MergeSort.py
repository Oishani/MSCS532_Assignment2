"""
Implementation of the Merge Sort algorithm.
Merge Sort is a stable, divide-and-conquer sorting algorithm with consistent O(n log n) performance.
"""

def merge_sort(arr):
    """
    Sorts the input list using the merge sort algorithm.

    Args:
        arr (list): List of comparable elements to be sorted.

    Returns:
        list: New sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Recursively sort the left and right halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): Sorted left half.
        right (list): Sorted right half.

    Returns:
        list: Merged sorted list.
    """
    merged = []
    i = j = 0

    # Compare and merge elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
