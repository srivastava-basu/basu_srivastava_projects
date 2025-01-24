#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
### PROBLEM STATEMENT ###
# You are given an array arr of numbers. Return the sum of all the elements except the first and last elements.
# Constraints:
#2<=arr.size()<=10^5
#2<=arr[i]<=10^5
class Solution:
    def sumExceptFirstLast(self,arr):
        # Parr:  list of pair
        #code here
        sum = 0
        if len(arr) <= 2:
            return sum
        else:
            for i in range(1,len(arr) - 1):
                sum += arr[i]
            return sum

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.sumExceptFirstLast(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends
