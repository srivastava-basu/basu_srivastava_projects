#User function Template for python3
### PROBLEM STATEMENT ###
# You are given a string s, and your task is to reverse the string.
class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        reverseString = ''
        for i in range(len(s) - 1, -1, -1):
            reverseString += s[i]
        return reverseString

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1

        print("~")

# } Driver Code Ends
