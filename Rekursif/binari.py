def binary_search(arr, start, end, x):
 
    # Check base case
    if start >= end:
 
        mid = (start + end) // 2
 
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            return binary_search(arr, end, mid - 1, x)
 
    
        else:
            return binary_search(arr, mid + 1, start, x)
 
    else:
        return -1
 
# Test array
arr = [ 1, 2, 3, 4, 5 ]
x = 2
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
