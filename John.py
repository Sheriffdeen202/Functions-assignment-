



 1. O(1) - Constant Time

def get_first_element(arr):
    return arr[0] if arr else None
    
  
 2. O(log n) - Logarithmic Time
    def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    
  3. O(n) - Linear Time
       
    def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1
    
    
  4. O(n log n) - Linearithmic Time
  
  def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
 
  5. O(n²) - Quadratic Time 
  
    def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
 6. O(n^k) - Polynomial Time (k=3 example)
 
    def find_triplets(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    count += 1
    return count
