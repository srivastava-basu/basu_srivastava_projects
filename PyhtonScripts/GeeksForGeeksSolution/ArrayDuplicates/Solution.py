### PROBLEM STATEMENT ###
#Given an array arr of integers, find all the elements that occur more than once in the array.
#If no element repeats, return an empty array.

class Solution:
    def findDuplicates(self, arr):
        # code here
        arr.sort()
        finalList =  []
        for i in range(0, len(arr)-1):
            if arr[i] == arr[i+1]:
                finalList.append(arr[i])
        finalList = list(dict.fromkeys(finalList))       
        return finalList



#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates
    # Sort the result in ascending order
    s.sort()
    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends
