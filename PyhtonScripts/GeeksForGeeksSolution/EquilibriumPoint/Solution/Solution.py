# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        totalRSum = sum(arr)
        tmpLSum = 0
        for i in range(len(arr)):
            totalRSum -= arr[i]
            if tmpLSum == totalRSum:
                return i
            tmpLSum += arr[i]
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
