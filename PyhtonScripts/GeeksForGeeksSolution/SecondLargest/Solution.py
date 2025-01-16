#User function Template for python3
### PROBLEM STATEMENT ###
#Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr = list(dict.fromkeys(arr))
        arr.sort()
        if len(arr) == 1:
            return -1
        else:
            return arr[-2]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
