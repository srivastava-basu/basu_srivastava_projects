#User function Template for python3
#You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).
class Solution:
    def getAlternates(self, arr):
        # Code Here
        finalList = []
        for i in range(0, len(arr)):
            if i%2 == 0:
                finalList.append(arr[i])
        return finalList

#{ 
 # Driver Code Starts
#Initial Template for Python 3
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    ls = Solution().getAlternates(arr)
    print(" ".join(map(str, ls)))
    print("~")

# } Driver Code Ends
