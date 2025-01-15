#User function Template for python3
### AUTHOR: BASU SRIVASTAVA ###
### Date Attempted: 15-JAN-2024 ###
### PROBLEM STATEMENT ###
# You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). 
#This array represents a permutation of the integers from 1 to n with one element missing. 
#Your task is to identify and return the missing element

class Solution:
    def missingNumber(self, arr):
        # code here
        # sorting the list for easy navigation
        arr.sort()
        #Condition for checking if it's a single element array with number 1
        if len(arr) == 1 and arr[0] == 1: 
            return (arr[0] + 1)
        #Condition for checking if it's a single element array with number 2
        elif len(arr) == 1 and arr[0] != 1:
            return 1    
        #elif arr[0] != 1:
        #   return 1    
        # Condition for checking any other missing number
        else: 
            for i in range(len(arr)):
                if i == len(arr) - 1:
                    return (arr[i] + 1)
                elif arr[i] == arr[i+1] - 1:
                    continue
                else:
                    return (arr[i] + 1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends
