Binary Search Approach: 
Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n). 
           else
               mid = (low + high) / 2 
                   if x == arr[mid]
                   return mid
       
               else if x > arr[mid]        // x is on the right side
                   return binarySearch(arr, x, mid + 1, high)
               
               else                        // x is on the left side
                   return binarySearch(arr, x, low, mid - 1) 
Illustration of Binary Search Algorithm: 





Example of Binary Search Algorithm

Recommended Practice
Binary Search
Try It!

Complete Interview Preparation - GFG

Step-by-step Binary Search Algorithm: We basically ignore half of the elements just after one comparison.

Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
Else (x is smaller) recur for the left half.
Recursive implementation of Binary Search:

# Python3 Program for recursive binary search.
 
# Returns index of x in arr if present, else -1
 
 

def binarySearch(arr, l, r, x):
 

    # Check base case

    if r >= l:
 

        mid = l + (r - l) // 2
 

        # If element is present at the middle itself

        if arr[mid] == x:

            return mid
 

        # If element is smaller than mid, then it

        # can only be present in left subarray

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
