# https://www.youtube.com/watch?v=qf82-r9hl2Y&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=9


def merge_sort_two_lists(a: list, b: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Args:
        a: The first sorted list.
        b: The second sorted list.

    Returns:
        C: The merged sorted list.
    """
    # Create a new list to store the merged list
    c = [0] * (len(a) + len(b))
    # Initialize variables to track the indices of lists A, B, and C
    i = k = n = 0
    # Merge the lists A and B into the list C
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
            print(a, b, c)  # Print the lists to debug the merging process
        else:
            c[n] = b[k]
            k += 1
            n += 1
            print(a, b, c)  # Print the lists to debug the merging process
    # Add the remaining elements of list A to the list C
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
        print(a, b, c)  # Print the lists to debug the merging process
    # Add the remaining elements of list B to the list C
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
        print(a, b, c)  # Print the lists to debug the merging process
    return c  # Return the merged sorted list


def merge_sort(a: list):
    """
    Sorts the given list using the merge sort algorithm.

    Args:
        a: The list to be sorted.

    Returns:
        None
    """
    # The base case.
    if len(a) <= 1:
        return
    # The recursive case.
    # Split the list into two halves
    middle = len(a) // 2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]
    # Recursively sort the two halves
    merge_sort(left)
    merge_sort(right)
    # Merge the sorted halves
    c = merge_sort_two_lists(left, right)
    # Copy the merged list back to the original list
    for i in range(len(a)):
        a[i] = c[i]

    return c


if __name__ == "__main__":
    one = [1, 3, 3, 5, 7]
    two = [2, 4, 6, 8]
    array = [10, 3, 12, 6, 2, 7, 10, 11, 13, 21, 19, 7]

    out = merge_sort_two_lists(one, two)
    print(out)

    out = merge_sort(array)
    print(out)
