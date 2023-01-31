# Skriven av Farhad Asadi

###############  Quicksort  ###############
import random

import sys
sys.setrecursionlimit(1000000)

#(i) Choose the first element as the pivot!
def partition_pivot_first(lst, first, last):
    """
    This function returns the index of the pivot.
    """
    pivot = lst[first]
    left = first + 1
    right = first + 1
    while right <= last:
        if lst[right] < pivot:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
        right += 1
    lst[first], lst[left-1] = lst[left-1], lst[first]
    return left - 1

def quicksort_first(lst, first, last):
    """
    This function sorts an array using the first element as the pivot.
    """
    if first < last:
        pivot_index = partition_pivot_first(lst, first, last)
        quicksort_first(lst, first, pivot_index-1)
        quicksort_first(lst, pivot_index + 1, last)

def quicksort_pivot_first(lst):
    """
    This function sorts an array using the first element as the pivot.
    """
    first = 0
    last = len(lst) - 1
    quicksort_first(lst, first, last)

# (ii) Median of three
def median(lst, first, middle, last):
    """
    This function sorts first, middle and last and then returns the element in the middle.
    """
    first_element = lst[first]
    middle_element = lst[middle]
    last_element = lst[last]
    if first_element > middle_element:
        if middle_element > last_element:
            return middle
        if first_element < last_element:
            return first
        return last
    if first_element > last_element:
        return first
    if middle_element < last_element:
        return middle
    return last

def partition_median_of_three(lst, first, last):
    """
    This function returns the index of the pivot
    """
    pivot = lst[last]
    i = first-1
    for j in range(first, last):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[last] = lst[last], lst[i+1]
    return i + 1

def quicksort_median(lst, first, last):
    """
    This function sorts an array using the mdian of three method.
    """
    if first < last:
        middle_index = (last + first) // 2
        median_index = median(lst, first, middle_index, last)
        # swap the pivot with the last element in the list
        lst[median_index], lst[last] = lst[last], lst[median_index]
        pivot  = partition_median_of_three(lst, first, last)
        quicksort_median(lst, first, pivot  - 1)
        quicksort_median(lst, pivot  + 1, last)

def quicksort_pivot_median(lst):
    quicksort_median(lst, 0, len(lst)-1)

###############  d-Heapsort  ###############

def heapify(lst, d, i, len_lst):
    """
    Heapify function for heapsort function.
    """
    largest_index = i
    for j in range(1, d+1):
        child = d*i + j
        if child < len_lst and lst[child] > lst[largest_index]:
            largest_index = child
    if largest_index != i:
        lst[largest_index], lst[i] = lst[i], lst[largest_index]
        heapify(lst, d, largest_index, len_lst)

def max_heap(lst, d):
    """
    Max heap function for heapsort.
    """
    for i in range((len(lst)-2//d), -1, -1):
        heapify(lst, d, i, len(lst))

def heapsort(lst, d = 2):
    """
    This function sorts an array using heapify and max_heap functions.
    """
    max_heap(lst, d)
    for i in range(len(lst)-1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, d, 0, i)



lst = random.sample(range(1000000), 100000)
lst.sort(reverse=True)
#lst.sort()
#heapsort(lst, 4)
#print(len(lst))
#heapsort(lst, 4)
quicksort_pivot_first(lst)

#quicksort_pivot_median(lst)

def merge_Sort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        if len(L) < 53:
            insertion_sort(L)
        else:
            merge_sort(L)

        if len(R) < 53:
            insertion_sort(R):
        else:
            merge_sort(R)

        # Everything else the same



def merge_hybrid(array):
    if len(array) < 52:
        insertion_sort(array)
    else:
        merge_sort(array)



def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        #mergeSort(L)
        #mergeSort(R)
        if len(L) < 53:
            insertion_sort(L)
        else:
            mergeSort(L)

        if len(R) < 53:
            insertion_sort(R)
        else:
            mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
