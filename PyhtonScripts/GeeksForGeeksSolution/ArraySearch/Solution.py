#User function Template for python3
#RROBLEM STATEMENT
#------------------
#Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. 
#Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
#------------------

class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        index = -1
        for i in range(len(arr)):
            if x == arr[i]:
                index = i
                break
        return index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        x = int(input())
        ob = Solution()
        print(ob.search(A, x))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
