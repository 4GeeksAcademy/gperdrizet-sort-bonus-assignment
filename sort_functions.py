"""
Sort Functions Module

This module contains implementations of various sorting algorithms for performance comparison.
Each function sorts a list of numbers using a different approach.
"""

import numpy as np
from typing import List


def builtin_sort(nums: List) -> List:
    """
    Sorts a list using Python's built-in sorted() function.
    
    Uses Timsort algorithm, which is a hybrid stable sorting algorithm derived from 
    merge sort and insertion sort. It performs well on real-world data by identifying 
    existing ordered subsequences and merging them efficiently. Has O(n log n) worst-case 
    time complexity but often performs better on partially sorted data.
    
    Args:
        nums: List of numbers to sort
        
    Returns:
        New sorted list
    """
    return sorted(nums)


def numpy_sort(nums: List) -> List:
    """
    Sorts a list using NumPy's sort function.
    
    Converts the input list to a NumPy array and uses NumPy's optimized sorting 
    algorithm (typically quicksort for numeric data). The algorithm is implemented 
    in C for better performance on large numerical datasets. Has O(n log n) average 
    time complexity but includes overhead from list-to-array conversion.
    
    Args:
        nums: List of numbers to sort
        
    Returns:
        New sorted list
    """
    nums_array = np.array(nums)
    return np.sort(nums_array).tolist()


def bubble_sort(nums: List) -> List:
    """
    Sorts a list using the bubble sort algorithm.
    
    Repeatedly steps through the list, compares adjacent elements and swaps them 
    if they are in the wrong order. The pass through the list is repeated until 
    the list is sorted. Called "bubble sort" because smaller elements "bubble" 
    to the beginning of the list. Has O(n²) time complexity, making it inefficient 
    for large datasets but useful for educational purposes.
    
    Args:
        nums: List of numbers to sort
        
    Returns:
        New sorted list
    """
    nums = nums.copy()  # Don't modify the original list
    n = len(nums)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    return nums


def merge_sort(nums: List) -> List:
    """
    Sorts a list using the merge sort algorithm.
    
    Implements a divide-and-conquer approach that recursively divides the list 
    into halves until each sublist contains only one element, then merges the 
    sublists back together in sorted order. Guarantees O(n log n) time complexity 
    in all cases (best, average, and worst) and is stable, maintaining the relative 
    order of equal elements.
    
    Args:
        nums: List of numbers to sort
        
    Returns:
        New sorted list
    """
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge(left, right)


def merge(left: List, right: List) -> List:
    """
    Helper function for merge sort to merge two sorted lists.
    
    Takes two already-sorted lists and combines them into a single sorted list 
    by comparing the first elements of each list and selecting the smaller one. 
    This process continues until all elements from both lists are merged.
    
    Args:
        left: First sorted list
        right: Second sorted list
        
    Returns:
        Merged sorted list containing all elements from both input lists
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result
