"""Sort Algorithms"""


def insertion_sort(items, gap=1):
    """
    1. copy the first of unsorted items to temp
    2. shift sorted items that are less than the key to the right
    3. insert the key into the blank position
    4. repeat above steps for the remaining unsorted items

    The `gap` argument is for shell sort insertion.
    """
    for i in range(gap, len(items)):
        temp, j = items[i], i
        while j >= gap and items[j - gap] > temp:
            items[j] = items[j - gap]
            j -= gap
        items[j] = temp


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


def selection_sort_recursive(items):
    """
    Be careful recursively selection sort cannot work for many items!
    """
    def _sort(items, i, n):
        if i < n - 1:
            least = i
            for j in range(i + 1, n):
                if items[j] < items[least]:
                    least = j
            if least != i:
                items[i], items[least] = items[least], items[i]
            _sort(items, i + 1, n)

    _sort(items, 0, len(items))


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

    def partition(items, start, end):
        pivot = items[end]
        p = start
        for i in range(start, end):
            if items[i] < pivot:
                items[i], items[p] = items[p], items[i]
                p += 1
        items[p], items[end] = items[end], items[p]
        return p

    def qs(items, start, end):
        if start < end:
            pivot = partition(items, start, end)
            qs(items, start, pivot - 1)
            qs(items, pivot + 1, end)

    qs(items, 0, len(items) - 1)


def quick_sort(items):
    """
    Quick sort with O(n) auxiliry 
    """
    length = len(items)
    if length <= 1:
        return items
    # Use the last element as the first pivot
    pivot = items.pop()
    # Put elements greater than pivot in greater list
    # Put elements lesser than pivot in lesser list
    greater, lesser = [], []
    for item in items:
        if item > pivot:
            greater.append(item)
        else:
            lesser.append(item)
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


def shell_sort(items):
    # Marcin Ciura's gap sequence
    for gap in [701, 301, 132, 57, 23, 10, 4, 1]:
        insertion_sort(items, gap=gap)


def heap_sort(items):
    """
    Assume the sequence of items as a full binary tree:
    1. bottom-up heapify the full binary tree to build a max heap
    2. swap the heap top (max item in unsorted portion) with the nth-last item
    to extend the sorted partition
    3. heapify the remaining unsorted partition
    """
    def heapify(items, start, end):
        """
        Swap the wrong top all the way down to the right position.
        This function is meaningful for a TOP-INCORRECT ONLY heap!
        """
        parent = start
        while parent * 2 + 1 <= end:
            child = parent * 2 + 1
            if child < end:
                # if parent has both left and right child
                # then choose the greater one
                child += (items[child] < items[child + 1])
            if items[parent] >= items[child]:
                # top is greater than both children, ready for swapping top
                # with current parent
                break
            # swap the value of current node with its larger child
            # then move parent to its larger child
            items[parent], items[child] = items[child], items[parent]
            parent = child

    n = len(items)
    for i in range(n // 2 - 1, -1, -1):
        heapify(items, i, n - 1)
    for i in range(n - 1, 0, -1):
        items[0], items[i] = items[i], items[0]
        heapify(items, 0, i - 1)
