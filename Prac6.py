import random
import matplotlib.pyplot as plt


def generate_random_list(n):
    return [random.randint(1, 1000) for _ in range(n)]

def merge_sort(arr):
    count = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        count += merge_sort(left_half)
        count += merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            count += 1
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

    return count


def BubbleSort(nums1):
    count = 0
    for i in range(1,len(nums1)):
        for j in range(0,len(nums1)-i):
            count+=1
            if nums1[j] > nums1[j+1]:
                [nums1[j],nums1[j+1]] = [nums1[j+1],nums1[j]]

    return count

def InsertionSort(nums2):
    count = 0
    for i in range(1,len(nums2)):
        key = nums2[i]
        j = i - 1
        while j>=0 and (nums2[j] > key):
            count+=1
            nums2[j+1] = nums2[j]
            j-=1
        nums2[j+1] = key
    return count


sorting_algorithms = [InsertionSort, BubbleSort, merge_sort]
algorithm_names = ["Insertion Sort", "Bubble sort", "Merge Sort"]

input_sizes = [10, 50, 100, 500, 1000, 1500, 2000, 2500]

steps_taken = {name: [] for name in algorithm_names}

for n in input_sizes:
    unsorted_list = generate_random_list(n)

    for algorithm, name in zip(sorting_algorithms, algorithm_names):
        arr = unsorted_list.copy()
        steps = algorithm(arr)
        steps_taken[name].append(steps)

plt.figure(figsize=(10, 6))
for name in algorithm_names:
    plt.plot(input_sizes, steps_taken[name], label=name)

plt.xlabel('Number of Elements (n)')
plt.ylabel('Steps Taken')
plt.title('Comparison of Sorting Algorithms based on Steps Taken')
plt.legend()
plt.grid(True)
plt.show()
