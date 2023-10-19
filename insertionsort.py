import sys
import time
import random
#sorting time comparison for CS 

#insertion sort
def insertionSort(arr):
    start_time = time.perf_counter()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    stop_time = time.perf_counter()
    print('Insertion time: ' + str(float(stop_time - start_time))+' ms')


#selection sort
def selectionSort(arr):
    start_time = time.perf_counter()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j      
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    stop_time = time.perf_counter()
    print('Selection time: ' + str(float(stop_time - start_time))+' ms')


#heap sort
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heapSort(arr):
    start_time = time.perf_counter()
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    stop_time = time.perf_counter()
    print('Heap time: ' + str(float(stop_time - start_time))+' ms')

    
#merge sort
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
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

#driver
array=[]
amount=10000
for i in range (amount):
    i = random.randint(0,amount*5)
    array.append(i)
insertionSort(array)
selectionSort(array)
heapSort(array)
#merge recursion
sys.setrecursionlimit(10000)
start_time = time.perf_counter()
mergeSort(array)
stop_time = time.perf_counter()
sys.setrecursionlimit(1000)
print('Merge time: ' + str(float(stop_time - start_time))+' ms')
