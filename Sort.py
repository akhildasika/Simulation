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




A = [64, 25, 12, 22, 11] 
  
 
for i in range(len(A)): 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
       
    A[i], A[min_idx] = A[min_idx], A[i] 
  

print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),  
