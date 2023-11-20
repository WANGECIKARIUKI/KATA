#Given an array of integers, arr, find out 2 indices m, n(0<=m<=arr.length-1, 
#0<=n<=arr.length-1, m<=n), so that as long as all elements in the subarray(from index m to n, 
#indices m and n inclusive) are sorted properly, with this sorted subarray relacing original subarray, 
#the whole array is sorted (no matter ascendingly or descendingly).

#The subarray should include the least number of elements, 
#means (n-m) must be of the smallest value, and n should also be the smallest one.

#The function accept an array of integers, arr, 
#reutrn the subarray's start and end index in array format, [m,n] as a result.

#For example, in an array [1,2,3,6,4,4], 
#the SMALLEST(with the least numbers of integers) subarray to be found is [6,4,4], 
#if we sort it to [4,4,6], then replace the original subarray, the whole array now turns to be[1,2,3,4,4,6], which is sorted completely.
#This subarray begins from index 3, and ends in index 5, so the result is [3,5].


def array(arr):
    #create a condition to check if the array is sorted
    if all(arr[i] == arr[0] 
           for i in range(len(arr))):
        return [0, 0]

   
    #if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        #return [0, 0]

   #find array positions where it starts and ends
    start, end = 0, len(arr) - 1
    while start < len(arr) - 1 and arr[start] <= arr[start + 1]:
        start += 1
    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    #find the min and max values in the subarray
    min = min(arr[start:end+1]),
    max = max(arr[start:end+1]),

    #include more elements in the subarray
    while end > 0 and arr[end - 1] > min:
        end -= 1
    while start < len(arr) - 1 and arr[start + 1] < max:
        start += 1

    return [start, end]

# Examples
arr0 = [5, 4, 9, 2, 1]
arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr2 = [9, 8, 7, 6, 5, 4, 3, 2]
