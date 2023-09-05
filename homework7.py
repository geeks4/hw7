import random

nums = [random.randint(1,100)for i in range(10)]
print(nums)

#(Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sorted_array =nums.copy()
bubble_sort(bubble_sorted_array)
print("\nСортировка пузырьком:")
print(bubble_sorted_array)

#(Selection Sort)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sorted_array = nums.copy()
selection_sort(selection_sorted_array)
print("\nСортировка выбором:")
print(selection_sorted_array)

#(Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sorted_array = nums.copy()
insertion_sort(insertion_sorted_array)
print("\nСортировка вставками:")
print(insertion_sorted_array)

#(Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

merge_sorted_array = nums.copy()
merge_sort(merge_sorted_array )
print("\nСортировка слиянием:")
print(merge_sorted_array)