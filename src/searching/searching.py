# Returns index of target in arr if present, else -1 
def binary_search(arr, target, start, end):
    # Base case
    while start <= end:
        middle = (start + end) // 2
        guess = arr[middle]

        # If element is present at the middle itself 
        if guess == target:
            return middle
        
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        if guess > target:
            return binary_search(arr, target, start, middle - 1) 
        
        # Else the element can only be present in right subarray 
        else:
            return binary_search(arr, target, middle + 1, end) 
    return -1  # not found


# # STRETCH: implement an order-agnostic binary search
# # This version of binary search should correctly find 
# # the target regardless of whether the input array is
# # sorted in ascending order or in descending order
# # You can implement this function either recursively 
# # or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

