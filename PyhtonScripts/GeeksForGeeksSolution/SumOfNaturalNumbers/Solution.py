# Sum of Natural Numbers
# Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum = 0
        for i in range(1, n+1):
            sum = sum + i
        return sum



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)
        print("~")

# } Driver Code Ends
