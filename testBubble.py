import sys

def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
               arr[j], arr[j+1] = arr[j+1], arr[j]

arr1 = [64, 34, 22, 11, 90]
arr2 = [64, 34, 22, 11]
arr3 = [-64, 34, 22]
arr4 = []

bubbleSort(arr1)
bubbleSort(arr2)
bubbleSort(arr3)
bubbleSort(arr4)

print(arr1)
print(arr2)
print(arr3)
print(arr4)




