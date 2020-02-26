"""Sort Algorithms"""


def insertion_sort(items):
    """
    1. copy the first of unsorted items to key
    2. shift sorted items that are less than the key to the right
    3. insert the key into the blank position
    4. repeat above steps for the remaining unsorted items
    """
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and key < items[j]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key


def selection_sort(items):
    """
    1. find the minimum item in unsorted items
    2. swap the item with the first unsorted item if they are different
    3. repeat above steps for the remaining unsorted items
    """
    length = len(items)
    for i in range(length - 1):
        least = i
        for j in range(i + 1, length):
            if items[j] < items[least]:
                least = j
        if least != i:
            items[i], items[least] = items[least], items[i]


def bubble_sort(items):
    """
    1. iterate over unsorted items, if one is greater than its right neighbor
       then swap them
    2. every iteration put the max unsorted item to the tail of sequence
    3. repeat above steps for the remaining unsorted items
    """
    length = len(items)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if items[j] > items[j + 1]:
                swapped = True
                items[j], items[j + 1] = items[j + 1], items[j]
        if not swapped:
            break


def merge_sort(items):
    """
    Merge sort evenly split the input array into two shallow copies.
    """

    def merge(left, right):
        """
        Merge two arrays into one with asending order.
        This function mutates inputs and returns a new array.
        """
        result = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        return result + left[left_idx:] + right[right_idx:]

    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


def quick_sort_in_place(items):
    """
    Quick sort in-place version with O(log n) space complexity
    """
    def qs(items, start, end):
        if start < end:
            pivot = partition(items, start, end)
            qs(items, start, pivot - 1)
            qs(items, pivot + 1, end)

    def partition(items, start, end):
        pivot = start
        for i in range(start, end):
            if items[i] < items[end]:
                items[i], items[pivot] = items[pivot], items[i]
                pivot += 1
        items[pivot], items[end] = items[end], items[pivot]
        return pivot

    qs(items, 0, len(items) - 1)


def quick_sort(collection):
    """
    Quick sort with O(n) auxiliry 
    """
    length = len(collection)
    if length <= 1:
        return collection
    else:
        # Use the last element as the first pivot
        pivot = collection.pop()
        # Put elements greater than pivot in greater list
        # Put elements lesser than pivot in lesser list
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        return [*quick_sort(lesser), pivot, *quick_sort(greater)]
