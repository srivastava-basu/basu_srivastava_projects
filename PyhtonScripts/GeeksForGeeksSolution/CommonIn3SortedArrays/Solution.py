#User function Template for python3
### PROBLEM STATEMENT ###
#You are given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
#If there are no such elements return an empty array. In this case, the output will be -1.

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        resultSet = set(arr1) & set(arr2) & set(arr3)
        finalList = list(resultSet)
        if len(finalList) == 0:
            finalList.append(-1)
            return finalList
        else:
            finalList.sort()
            return finalList


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))
        print("~")
# } Driver Code Ends
