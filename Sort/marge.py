# import random
# import time

# def mergesort(num, temp, N):
#     start_time = time.time()  # Catat waktu awal
#     m_sort(num, temp, 0, N - 1)
#     end_time = time.time()  # Catat waktu akhir
#     execution_time = end_time - start_time  # Hitung waktu eksekusi
#     return execution_time

# def m_sort(num, temp, left, right):
#     if right > left:
#         mid = (right + left) // 2
#         m_sort(num, temp, left, mid)
#         m_sort(num, temp, mid + 1, right)
#         merge(num, temp, left, mid + 1, right)

# def merge(num, temp, left, mid, right):
#     left_end = mid - 1
#     tmp_pos = left
#     num_el = right - left + 1

#     while left <= left_end and mid <= right:
#         if num[left] <= num[mid]:
#             temp[tmp_pos] = num[left]
#             tmp_pos += 1
#             left += 1
#         else:
#             temp[tmp_pos] = num[mid]
#             tmp_pos += 1
#             mid += 1

#     while left <= left_end:
#         temp[tmp_pos] = num[left]
#         left += 1
#         tmp_pos += 1

#     while mid <= right:
#         temp[tmp_pos] = num[mid]
#         mid += 1
#         tmp_pos += 1

#     for i in range(num_el):
#         num[right] = temp[right]
#         right -= 1

# # Generate random input
# N = 100000  # Jumlah elemen dalam array
# num = [random.randint(1, 1000) for _ in range(N)]
# temp = [0] * N  # Inisialisasi array temp

# print("Given array:", num)

# # Sort array and measure execution time
# execution_time = mergesort(num, temp, N)

# print("Sorted array:", num)
# print("Execution time:", execution_time, "seconds")



# Python program for implementation of MergeSort
import time
import random

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    # Generate random array with 1000 elements
    arr = [random.randint(1, 100) for _ in range(10000)]
    print("Given array is")
    printList(arr)
    
    start_time = time.time()  # Start time measurement
    mergeSort(arr)
    end_time = time.time()  # End time measurement
    
    print("\nSorted array is ")
    printList(arr)
    
    execution_time = end_time - start_time  # Calculate execution time in seconds
    print("Execution time:", execution_time, "seconds") 