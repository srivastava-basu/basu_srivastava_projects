#User function Template for python3

class Solution:
    def getDigitDiff1AndLessK(self, arr, k):
        # code here
        finalList = []
        for a in arr:
            if a < k and a > 9:
                flag = True
                numInString = str(a)
                for b in range(len(numInString)-1):
                    if abs(int(numInString[b])-int(numInString[b+1]))!=1:
                        flag = False
                        break
                if flag:
                    finalList.append(a) 
        return finalList

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getDigitDiff1AndLessK(arr, k)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
