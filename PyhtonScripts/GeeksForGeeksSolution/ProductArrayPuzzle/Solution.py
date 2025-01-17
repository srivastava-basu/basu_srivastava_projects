#User function Template for python3
#Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. 
#Return this resultant array, res[].
#Note: Each element is res[] lies inside the 32-bit integer range.

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        res = [1]*len(arr)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
        suffix = 1
        for j in range(n-1, -1, -1):
            res[j] *= suffix
            suffix *= arr[j]
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends
