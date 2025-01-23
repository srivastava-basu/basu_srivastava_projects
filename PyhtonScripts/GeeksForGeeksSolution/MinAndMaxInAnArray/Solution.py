#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3
### PROBLEM STATEMENT ###
# Given an array arr. Your task is to find the minimum and maximum elements in the array.
#Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.

class Solution:
    def get_min_max(self, arr):
        min = arr[0]
        max = 0
        for i in range(0, len(arr)):
            if max <= arr[i]:
                max = arr[i]
            elif min >= arr[i]:
                min = arr[i]
        return min, max
        #Below soultion is using in-built functions
        #return min(arr), max(arr)
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1
        print("~")


# } Driver Code Ends
