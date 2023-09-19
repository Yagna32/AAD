import matplotlib.pyplot as plt

nums = list(map(int,input("Enter list of numbers : ").split(' ')))

num1 = nums.copy()
num2 = nums.copy()
nums3 = nums.copy()
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

algorithms = ["Merge sort","bubble sort","Insertion sort"]

plt.plot(algorithms,[merge_sort(num1),BubbleSort(num2),InsertionSort(nums3)],c='c',marker='o')
plt.xlabel('sorting algorithms')
plt.ylabel('comparision count')
plt.title('Sorting algorithm analysis')
plt.grid(True)
plt.show()