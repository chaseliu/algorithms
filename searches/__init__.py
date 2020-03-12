"""Search Algorithms"""


def interpolation_search(arr, item):
    low, high = 0, len(arr) - 1
    while low <= high:
        # avoid divided by 0 during interpolation
        if arr[low] == arr[high]:
            return low if arr[low] == item else -1
        # mid will be the left most occurance
        mid = low + (item - arr[low]) * (high - low) // (arr[high] - arr[low])
        if arr[mid] < item:
            high = mid - 1
        elif arr[mid] > item:
            low = mid + 1
        else:
            return mid
    return -1
