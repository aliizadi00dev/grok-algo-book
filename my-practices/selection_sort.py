
MY_LIST = [23, 98, 1, 7, 239]


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        print(f"> find_smallest >> for [begin] at index {i}")
        if arr[i] < smallest:
            print(f">> find_smallest >> for [inside] >> if {arr[i]} < {smallest}={
                  arr[i] < smallest}")
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# result = find_smallest(MY_LIST)
# print(result)


def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        print(f"> selection_sort >> for [begin] at index {_}")
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort(MY_LIST))
