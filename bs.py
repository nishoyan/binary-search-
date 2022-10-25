
 

def binarySearch(arr, l, r, x):

    if r >= l:
 

        mid = l + (r - l) // 2

        if arr[mid] == x:

            return mid

        elif arr[mid] > x:

            return binarySearch(arr, l, mid-1, x)
 

        # Else the element can only be present

        # in right subarray

        else:

            return binarySearch(arr, mid + 1, r, x)
 

    else:

        return -1
 
 
# Driver Code

arr = [2, 3, 4, 10, 40]

x = 10
 
# Function call

result = binarySearch(arr, 0, len(arr)-1, x)
 

if result != -1:

    print("Element is present at index % d" % result)

else:

    print("Element is not present in array")
