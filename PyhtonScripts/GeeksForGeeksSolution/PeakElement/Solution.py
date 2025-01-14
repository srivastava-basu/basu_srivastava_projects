#Given an array arr[] where no two adjacent elements are same, find the index of a peak element. 
#An element is considered to be a peak if it is greater than its adjacent elements (if they exist). 
#If there are multiple peak elements, return index of any one of them. 
#The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".
#Note: Consider the element before the first element and the element after the last element to be negative infinity.

class Solution:   
    def peakElement(self,arr):
        # Code here
        index = -1
        if len(arr) == 1:
            index = 0
        else:
            for i in range(0,len(arr)):
                if (i == len(arr) - 1) and (arr[i] > arr[i-1]):
                    index = i
                    break
                elif i == 0 and arr[i] > arr[i+1]:
                    index = i
                    break
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    index = i
                    break
        return index


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
